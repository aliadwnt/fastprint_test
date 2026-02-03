import requests
import hashlib

def fetch_fastprint_products():
    url = "https://recruitment.fastprint.co.id/tes/api_tes_programmer"

    raw_pass = "bisacoding-2-2-26"
    password = hashlib.md5(raw_pass.encode()).hexdigest()

    response = requests.get(
        url,
        headers={
            "username": "tesprogrammer040226C01",
            "password": password
        }
    )

    response.raise_for_status()
    return response.json()
