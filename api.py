import json
from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.exception.tencent_cloud_sdk_exception import (
    TencentCloudSDKException,
)
from tencentcloud.aai.v20180522 import aai_client, models
import os
import traceback
import base64


def createCredential() -> credential.Credential:
    secret_id = os.getenv("TC_SECRETID")
    secret_key = os.getenv("TC_SECRETKEY")
    return credential.Credential(secret_id, secret_key)


def transform(text: str, cred: credential.Credential = createCredential()) -> bytes:
    try:
        httpProfile = HttpProfile()
        httpProfile.endpoint = "aai.tencentcloudapi.com"

        clientProfile = ClientProfile()
        clientProfile.httpProfile = httpProfile
        client = aai_client.AaiClient(cred, "ap-shanghai", clientProfile)

        req = models.TextToVoiceRequest()
        params = {
            "Text": text,
            "SessionId": "2021年5月11日",
            "SampleRate": 8000,
            "Codec": "mp3",
            "ModelType": 1,
        }
        req.from_json_string(json.dumps(params))

        resp = client.TextToVoice(req)
        raw = resp.to_json_string()
        data = json.loads(raw)
        audio = data["Audio"].encode()
        return base64.b64decode(audio)

    except TencentCloudSDKException as err:
        traceback.print_exc()
        return b""
