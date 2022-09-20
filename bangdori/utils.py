import hashlib
import hmac
import base64
import os
from dotenv import load_dotenv
def make_signature(timestamp):
    load_dotenv()

    access_key = os.getenv('ncloud_private_Accesskey')
    secret_key = os.getenv('ncloud_private_Secretkey')

    secret_key = bytes(secret_key, 'UTF-8')

    uri = "/sms/v2/services/ncp:sms:kr:292652557635:sms_auth/messages"
    # uri 중간에 Console - Project - 해당 Project 서비스 ID 입력 (예시 = ncp:sms:kr:263092132141:sms)

    message = "POST" + " " + uri + "\n" + timestamp + "\n" + access_key
    message = bytes(message, 'UTF-8')
    signingKey = base64.b64encode(
        hmac.new(secret_key, message, digestmod=hashlib.sha256).digest())
        
    return signingKey
