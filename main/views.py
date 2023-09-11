from django.shortcuts import render

# Create your views here.
def main_view(request):
    context = {
        "Nama_Aplikasi": "Inventory RPG",
        "Nama": "Thirza Ahmad Tsaqif",
        "Class": "PBP E",
        "Inventory" : [
            {"name": "Boeing 737",
             "amount": "10",
             "description": "Pesawat Komersial Boeing 737",
             "engine": "Rolls Royce",
             "winglet": "True"
             },
            {"name": "Boeing 747",
             "amount": "10",
             "description": "Pesawat Komersial Boeing 747",
             "engine": "4",
             "winglet": "True"
             }
        ]
    }
    return render(request, "main.html", context)