import os

from tencentcloud.common import credential


def createCredential() -> credential.Credential:
    secret_id = os.getenv("secretid")
    secret_key = os.getenv("secretkey")
    return credential.Credential(secret_id, secret_key)
