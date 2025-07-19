import os
import boto3
import pandas as pd
from tempfile import NamedTemporaryFile

def generate_and_upload_excel(job_id, columns, data):
    df = pd.DataFrame(data, columns=columns)

    with NamedTemporaryFile(delete=False, suffix=".xlsx") as tmp:
        file_path = tmp.name
        df.to_excel(file_path, index=False)

    s3 = boto3.client(
        's3',
        aws_access_key_id=os.environ["ARVAN_ACCESS_KEY"],
        aws_secret_access_key=os.environ["ARVAN_SECRET_KEY"],
        endpoint_url=os.environ["ARVAN_ENDPOINT"],  # e.g. https://s3.ir-thr-at1.arvanstorage.ir
    )

    bucket = os.environ["ARVAN_BUCKET"]
    s3_key = f"exports/{job_id}.xlsx"

    s3.upload_file(file_path, bucket, s3_key, ExtraArgs={'ACL': 'public-read'})

    return f"{os.environ['ARVAN_PUBLIC_URL']}/{s3_key}"
