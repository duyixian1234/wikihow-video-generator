from qcloud_cos import CosClientError, CosConfig, CosS3Client, CosServiceError

from credential import createCredential


def createClient() -> CosS3Client:
    cred = createCredential()
    CosConfig(Secret_id=cred.secretId, Secret_key=cred.secretKey, Region="ap-shanghai")
    config = CosConfig(
        Secret_id=cred.secretId, Secret_key=cred.secretKey, Region="ap-shanghai"
    )
    client = CosS3Client(config)
    return client


def putObject(client: CosS3Client, bucket: str, body: bytes, key: str):
    resp = client.put_object(Bucket=bucket, Body=body, Key=key, EnableMD5=True)


def loadObject(client: CosS3Client, bucket: str):
    resp = client.list_objects(Bucket=bucket)
