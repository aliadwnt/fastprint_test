from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.db.models import Q
from django.db.models.functions import Lower

from produk.models import Produk, Kategori, Status
from produk.forms.produkForm import ProdukForm
from produk.services.apiService import fetch_produk_api


def index(request):
    q = request.GET.get('q', '').strip()
    status = request.GET.get('status', '').strip()

    # produk = Produk.objects.filter(
    #     status__nama_status__iexact="bisa dijual"
    # )
    
    # tampilin semua status produk
    produk = Produk.objects.all()

    #tampilin berdasarkan filter status
    if status == "semua":
        produk = Produk.objects.all()
    elif status:
        produk = Produk.objects.filter(
            status__nama_status__iexact=status
        )

    # Search nama produk
    if q:
        produk = produk.annotate(
            nama_lower=Lower('nama_produk')
        ).filter(
            nama_lower__contains=q.lower()
        )

    paginator = Paginator(produk, 10)
    page_number = request.GET.get('page')
    produk_page = paginator.get_page(page_number)

    status_list = Status.objects.all()

    return render(request, 'index.html', {
        'produk': produk_page,
        'status_list': status_list,
        'q': q,
        'status': status,
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