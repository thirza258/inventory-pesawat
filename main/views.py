from django.shortcuts import render
from main.forms import ItemForm
from django.http import HttpResponseRedirect, HttpResponse
from .models import Item
from django.core import serializers
from django.urls import reverse

# Create your views here.
def main_view(request):
    items = Item.objects.all()

    context = {
        "Nama_Aplikasi": "Inventory Pesawat",
        "Nama": "Thirza Ahmad Tsaqif",
        "Class": "PBP E",
        "Inventory" : items,
        "jumlah_item": len(items),
    }
    return render(request, "main.html", context)

def add_item(request):
    form = ItemForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse("main:main_view"))
    
    context = {"form": form}
    return render(request, "add_item.html", context)

def xml_format(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def xml_format_by_id(request, id):
    data = Item.objects.filter(id=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def json_format(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def json_format_by_id(request, id):
    data = Item.objects.filter(id=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

