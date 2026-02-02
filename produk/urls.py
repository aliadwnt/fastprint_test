from django.urls import path
from produk.controllers import produkController as pc

urlpatterns = [
    path('', pc.index, name='produk_index'),
    path('tambah/', pc.create),
    path('edit/<int:id>/', pc.edit),
    path('hapus/<int:id>/', pc.delete),
    path('sync-api/', pc.sync_api),
]
