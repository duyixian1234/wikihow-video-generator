import os
from tencentcloud.common import credential


def createCredential() -> credential.Credential:
    secret_id = os.getenv("TC_SECRETID")
    secret_key = os.getenv("TC_SECRETKEY")
    return credential.Credential(secret_id, secret_key)
