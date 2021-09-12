from google.cloud import bigquery
from config import BQ_DATASET, BQ_TABLE

client = bigquery.Client()

table = f'{client.project}.{BQ_DATASET}.{BQ_TABLE}'

def save(id, usd_eur):
    query = f"""
        INSERT INTO `{table}` (id, usd_eur) VALUES ({id}, {usd_eur})
    """
    client.query(query)