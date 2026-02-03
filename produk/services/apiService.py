import requests
import hashlib
from datetime import datetime
from django.conf import settings

def fetch_produk_api():
    url = "https://recruitment.fastprint.co.id/tes/api_tes_programmer"

    today = datetime.now()
    raw_password = (
        f"{settings.FASTPRINT_PASSWORD_PREFIX}-"
        f"{today.day:02d}-"
        f"{today.month:02d}-"
        f"{str(today.year)[-2:]}"
    )

    password = hashlib.md5(raw_password.encode()).hexdigest()

    payload = {
        "username": settings.FASTPRINT_USERNAME,
        "password": password
    }

    response = requests.post(url, data=payload)
    data = response.json()

    if data.get("error") == 1:
        raise Exception(f"FastPrint API Error: {data.get('ket')}")

    return data["data"]
