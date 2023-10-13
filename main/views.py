from django.shortcuts import render
from main.forms import ItemForm
from main.models import Item
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404
from django.core import serializers
from django.urls import reverse
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages  
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import datetime
from django.views.generic import UpdateView
from django.views.decorators.csrf import csrf_exempt 


# Create your views here.
@login_required(login_url='/login')
def main_view(request):
    items = Item.objects.filter(user = request.user)

    context = {
        "nama_aplikasi": "Inventory Pesawat",
        "nama": "Thirza Ahmad Tsaqif",
        "pengguna_login" : request.user.username,
        "class": "PBP E",
        "inventory" : items,
        "jumlah_item": len(items),
        "last_login": request.COOKIES['last_login'],
    }
    return render(request, "main.html", context)

def add_item(request):
    form = ItemForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        item = form.save(commit=False)
        item.user = request.user
        item.save()
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

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect("main:login")
    context = {"form":form}
    return render(request, "register.html", context)

def login_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("main:main_view")) 
            response.set_cookie("last_login", str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')
    context = {}
    return render(request, "login.html", context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

def add_amount(request, id):
    try:
        item = Item.objects.get(pk=id)
        item.amount += 1
        item.save()
        return HttpResponseRedirect(reverse('main:main_view'))
    except Item.DoesNotExist:
        return JsonResponse({'error': 'Item not found'}, status=404)

def sub_amount(request, id):
    try:
        item = Item.objects.get(pk=id)
        item.amount -= 1
        item.save()
        return HttpResponseRedirect(reverse('main:main_view'))
    except Item.DoesNotExist:
        return JsonResponse({'error': 'Item not found'}, status=404)

def delete_data(request, id):
    try:
        item = Item.objects.get(pk=id)
        item.delete()
        return HttpResponseRedirect(reverse('main:main_view'))
    except Item.DoesNotExist:
        return JsonResponse({'error': 'Item not found'}, status=404)


def get_item_json(request):
    items = Item.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize('json', items))

@csrf_exempt
def add_item_ajax(request):
    if request.method == "POST":
        user = request.user
        name = request.POST.get("name")
        amount = request.POST.get("amount")
        description = request.POST.get("description")
        engine = request.POST.get("engine")
        winglet = request.POST.get("winglet") == "true"
        image = request.POST.get("image")

        item = Item(user=user, name=name, amount=amount, description=description, engine=engine, winglet=winglet, image=image)
        item.save()

        return HttpResponse(b"Created", status=201)
    return HttpResponse("Not Found", status=404)

@csrf_exempt
def delete_item_ajax(request, id):
    if request.method == "DELETE":
        try:
            item = get_object_or_404(Item, pk=id)
            item.delete()
            return HttpResponse("Deleted", status=200)
        except Item.DoesNotExist:
            return HttpResponse({'error': 'Item not found'}, status=404)

@csrf_exempt
def add_amount_ajax(request, id):
    try:
        item = get_object_or_404(Item, pk=id)
        item.amount += 1
        item.save()
        return HttpResponse("Item Amount Added", status=200)
    except Item.DoesNotExist:
        return HttpResponse({'error': 'Item not found'}, status=404)
    
@csrf_exempt
def reduce_amount_ajax(request, id):
    try:
        item = get_object_or_404(Item, pk=id)
        item.amount -= 1
        item.save()
        return HttpResponse("Item Amount Reduced", status=200)
    except Item.DoesNotExist:
        return HttpResponse({'error': 'Item not found'}, status=404)