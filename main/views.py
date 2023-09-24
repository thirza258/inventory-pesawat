from django.shortcuts import render
from main.forms import ItemForm
from django.http import HttpResponseRedirect, HttpResponse
from main.models import Item
from django.core import serializers
from django.urls import reverse
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages  
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
@login_required(login_url='/login')
def main_view(request):
    items = Item.objects.all()

    context = {
        "user_login": request.user.username,
        "nama_aplikasi": "Inventory Pesawat",
        "nama": "Thirza Ahmad Tsaqif",
        "class": "PBP E",
        "inventory" : items,
        "jumlah_item": len(items),
        'last_login': request.COOKIES['last_login'],
    }
    return render(request, "main.html", context)

def add_item(request):
    form = ItemForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        product = form.save(commit=False)
        product.user = request.user
        product.save()
        return HttpResponseRedirect(reverse('main:main_view'))
    
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

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("main:main_view")) 
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

def add_amount(request, id):
    item = Item.objects.get(id=id)
    item.amount = item.amount + 1
    item.save()
    return HttpResponseRedirect(reverse('main:main_view'))

def delete_data(request, id):
    item = Item.objects.get(id=id)
    item.delete()
    return HttpResponseRedirect(reverse('main:main_view'))
