import pandas as pd
import json
import requests as r
import warnings
import logging
import time
import os
import datetime as dt


logging.basicConfig(
    level=logging.INFO,
    format=' %(asctime)s - %(name)-18s - %(levelname)-8s %(message)s',
    datefmt='%I:%M:%S %p')
logger = logging.getLogger(__name__)
warnings.filterwarnings('ignore')

APPEND_TOKEN = os.environ['APPEND_TOKEN']
READ_TOKEN = os.environ['READ_TOKEN']
URL = 'https://api.tinybird.co/v0/datasources'


def get_session(mode):

    session = r.Session()
    token = APPEND_TOKEN if mode == 'append' else READ_TOKEN
    session.headers = {'Authorization': 'Bearer ' + token}

    return session


def import_and_replace(dataset):

    logger.info(f'Importing {dataset} into tinybird...')

    s = get_session(mode='append')
    url = f'https://raw.githubusercontent.com/datadista/datasets/master/COVID%2019/ccaa_covid19_{dataset}_long.csv'
    params = {
        "name": f"ccaa_covid19_{dataset}",
        "mode": "replace",
        "url": url
    }

    try:
        r = s.post(
                url=URL,
                params=params
            )
        logger.info(f'{dataset} imported into tinybird!')
        return f'Success! {r.status_code}'
    except Exception as e:
        logger.info(f'Someting went wrong!')
        return f'Error!, {e}'
