from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator

from produk.models import Produk, Kategori, Status
from produk.forms.produkForm import ProdukForm
from produk.services.apiService import fetch_produk_api

def index(request):
    qs = Produk.objects.filter(
        status__nama_status__iexact="bisa dijual"
    ).order_by("nama_produk")

    paginator = Paginator(qs, 10)  # 10 data per halaman
    page_number = request.GET.get("page")
    produk = paginator.get_page(page_number)

    return render(request, "index.html", {
        "produk": produk
    })

def create(request):
    form = ProdukForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("produk_index")

    return render(request, "form.html", {
        "form": form
    })

def edit(request, id):
    produk = get_object_or_404(Produk, id=id)
    form = ProdukForm(request.POST or None, instance=produk)

    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("produk_index")

    return render(request, "form.html", {
        "form": form
    })

def delete(request, id):
    produk = get_object_or_404(Produk, id=id)
    produk.delete()
    return redirect("produk_index")
def sync_api(request):
    data = fetch_produk_api()

    for item in data:
        kategori, _ = Kategori.objects.get_or_create(
            nama_kategori=item["kategori"]
        )
        status, _ = Status.objects.get_or_create(
            nama_status=item["status"]
        )

        Produk.objects.update_or_create(
            nama_produk=item["nama_produk"],
            defaults={
                "harga": item["harga"],
                "kategori": kategori,
                "status": status
            }
        )

    return redirect("produk_index")


def import_produk(request):
    data = fetch_fastprint_products()

    for item in data:
        kategori, _ = Kategori.objects.get_or_create(
            nama_kategori=item['kategori']
        )
        status, _ = Status.objects.get_or_create(
            nama_status=item['status']
        )

        Produk.objects.create(
            nama_produk=item['nama_produk'],
            harga=item['harga'],
            kategori=kategori,
            status=status
        )

    return redirect('produk_list')
