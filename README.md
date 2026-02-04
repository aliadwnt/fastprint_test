# Test Junior Programmer – FastPrint

Project ini dibuat untuk memenuhi **Tes Junior Programmer FastPrint** menggunakan **Django**.

Aplikasi mengambil data produk dari API FastPrint, menyimpannya ke database, dan menampilkannya dalam bentuk tabel dengan fitur CRUD.

---

## Fitur

- Ambil data produk dari API FastPrint
- Simpan data ke database
- Tampilkan data produk
- Filter produk berdasarkan status
- Pencarian produk
- Tambah, edit, dan hapus produk
- Validasi form (nama wajib, harga angka)
- Konfirmasi saat hapus data

---

## Teknologi

- Python
- Django
- SQLite
- Tailwind CSS

---

## Cara Menjalankan

```bash
python -m venv env
env\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```
buka di browser:
http://127.0.0.1:8000/

---

## Dokumentasi Video
Youtube: https://youtu.be/i4O1iQ9efFM