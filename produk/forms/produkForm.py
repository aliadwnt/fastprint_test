from django import forms
from produk.models import Produk

class ProdukForm(forms.ModelForm):
    class Meta:
        model = Produk
        fields = '__all__'

    def clean_nama_produk(self):
        if not self.cleaned_data['nama_produk']:
            raise forms.ValidationError("Nama produk wajib diisi")
        return self.cleaned_data['nama_produk']

    def clean_harga(self):
        harga = self.cleaned_data['harga']
        if harga <= 0:
            raise forms.ValidationError("Harga harus angka")
        return harga
