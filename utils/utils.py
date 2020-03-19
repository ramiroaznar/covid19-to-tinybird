import pandas as pd
import json
from cartoframes.auth import set_default_credentials
from cartoframes import to_carto, read_carto
import warnings
import logging
import time
from carto.auth import APIKeyAuthClient
from carto.sql import BatchSQLClient
from carto.exceptions import CartoException


logging.basicConfig(
    level=logging.INFO,
    format=' %(asctime)s - %(name)-18s - %(levelname)-8s %(message)s',
    datefmt='%I:%M:%S %p')
logger = logging.getLogger(__name__)
warnings.filterwarnings('ignore')


set_default_credentials('creds.json')
with open('creds.json', 'r') as f:
    creds = json.load(f)
    USERNAME = creds['username']
    API_KEY = creds['api_key']
    USR_BASE_URL = "https://{user}.carto.com/".format(user=USERNAME)

auth_client = APIKeyAuthClient(api_key=API_KEY, base_url=USR_BASE_URL)
SQL_CLIENT = BatchSQLClient(auth_client)
DATASETS = ['casos', 'fallecidos', 'uci', 'altas']


def get_datasets():

    logger.info('Getting datasets...')

    URL = "https://raw.githubusercontent.com/datadista/datasets/master/COVID%2019/ccaa_covid19_{}.csv"

    datasets = (
        pd.read_csv(
            URL.format(i),
            index_col=0)
        for i in DATASETS
    )

    return datasets


def import_datasets_to_carto(dfs_obj):

    logger.info('Importing datasets into carto...')

    errors = []
    try:
        for k, v in dfs_obj.items():
            to_carto(v, k, if_exists='replace')
            time.sleep(60)

    except Exception as e:
        logger.info(e)
        errors.append(e)
        return errors


def read_sql_file(file_name):

    logger.info('Reading SQL file...')

    with open(f'sql/{file_name}.sql', 'r') as sql_file:
        sql = sql_file.read()

    sql_string = sql.replace("\r", "").replace("\n", "")

    return sql_string


def get_unnested_datasets():

    logger.info('Getting unnested datasets...')

    unnested_datasets = (
        read_carto(read_sql_file(f'unnest_{i}').format(dataset=i))
        for i in DATASETS
    )

    return unnested_datasets


def get_centroids_datasets():

    logger.info('Getting centroids datasets...')

    centroids_datasets = (
        read_carto(read_sql_file('centroids').format(dataset=i))
        for i in DATASETS
    )

    return centroids_datasets


def update_geoms():

    update_queries = []

    try:
        [update_queries.append(
            read_sql_file('update_geoms').format(dataset=i)
            )
            for i in DATASETS]
    except CartoException as e:
        logger.info("some error ocurred", e)

    job = SQL_CLIENT.create(update_queries)

    job_id = job['job_id']
    status = 'pending'
    while status != 'done':
        job = SQL_CLIENT.read(job_id)
        status = job['status']
        queries = job['query']
        logger.info(", ".join(map(lambda q: q['status'],queries)))
        time.sleep(60)

    return status
