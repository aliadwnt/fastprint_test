from django.db import models
from .kategoriModel import Kategori
from .statusModel import Status

class Produk(models.Model):
    nama_produk = models.CharField(max_length=200)
    harga = models.IntegerField()
    kategori = models.ForeignKey(Kategori, on_delete=models.CASCADE)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)

    def __str__(self):
        return self.nama_produk
