from django import forms
from produk.models import Produk

class ProdukForm(forms.ModelForm):
    class Meta:
        model = Produk
        fields = "__all__"
        widgets = {
            'nama_produk': forms.TextInput(attrs={
                'class': 'w-full px-4 py-2 border rounded-lg focus:ring-2 focus:ring-blue-500'
            }),
            'harga': forms.NumberInput(attrs={
                'class': 'w-full px-4 py-2 border rounded-lg focus:ring-2 focus:ring-blue-500'
            }),
            'kategori': forms.Select(attrs={
                'class': 'w-full px-4 py-2 border rounded-lg focus:ring-2 focus:ring-blue-500'
            }),
            'status': forms.Select(attrs={
                'class': 'w-full px-4 py-2 border rounded-lg focus:ring-2 focus:ring-blue-500'
            }),
        }
