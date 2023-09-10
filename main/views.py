from django.shortcuts import render

# Create your views here.
def main_view(request):
    context = {
        "Nama_Aplikasi": "Inventory RPG",
        "Nama": "Thirza Ahmad Tsaqif",
        "Class": "PBP E"
    }
    return render(request, "main.html", context)