import requests
import hashlib
from datetime import datetime
from produk.models import Produk, Kategori, Status


def fetch_produk_api():
    url = "https://recruitment.fastprint.co.id/tes/api_tes_programmer"

    today = datetime.now()
    raw_password = f"bisacoding-{today.day:02d}-{today.month:02d}-{str(today.year)[-2:]}"
    password = hashlib.md5(raw_password.encode()).hexdigest()

    payload = {
        "username": "tesprogrammer020226C22",
        "password": password
    }

    session = requests.Session()
    response = session.post(url, data=payload)

    data = response.json()

    print("STATUS:", response.status_code)
    print("RESPONSE:", data)

    if 'data' not in data:
        raise Exception(f"Gagal ambil data API: {data}")

    for item in data['data']:
        kategori, _ = Kategori.objects.get_or_create(
            nama_kategori=item['kategori']
        )

        status, _ = Status.objects.get_or_create(
            nama_status=item['status']
        )

        Produk.objects.update_or_create(
            nama_produk=item['nama_produk'],
            defaults={
                'harga': item['harga'],
                'kategori': kategori,
                'status': status
            }
        )
