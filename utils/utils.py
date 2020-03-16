import pandas as pd
import os
from cartoframes.auth import set_default_credentials
from cartoframes import to_carto, read_carto
import warnings
import logging


logging.basicConfig(
    level=logging.INFO,
    format=' %(asctime)s - %(name)-18s - %(levelname)-8s %(message)s',
    datefmt='%I:%M:%S %p')
logger = logging.getLogger(__name__)
warnings.filterwarnings('ignore')


set_default_credentials('creds.json')
DATASETS = ['casos', 'fallecidos']


def get_datasets():

    logger.info('Getting datasets...')

    URL = "https://raw.githubusercontent.com/datadista/datasets/master/COVID%2019/ccaa_covid19_{}.csv"

    casos, fallecidos = (
        pd.read_csv(
            URL.format(i),
            index_col=0)
        for i in DATASETS
    )

    return casos, fallecidos


def import_datasets_to_carto(dfs_obj):

    logger.info('Importing datasets into carto...')

    errors = []
    try:
        [to_carto(v, k, if_exists='replace')
        for k, v in dfs_obj.items()]
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

    sql_file = read_sql_file('unnest')
    
    unnested_casos, unnested_fallecidos = (
        read_carto(sql_file.format(dataset=i))
        for i in DATASETS
    )

    return unnested_casos, unnested_fallecidos


def get_centroids_datasets():

    logger.info('Getting centroids datasets...')

    centroids_casos, centroids_fallecidos = (
        read_carto(read_sql_file('centroids').format(i))
        for i in DATASETS
    )

    return centroids_casos, centroids_fallecidos
