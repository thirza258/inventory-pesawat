from django.shortcuts import render

# Create your views here.
def main_view(request):
    context = {
        "Nama_Aplikasi": "Inventory Pesawat",
        "Nama": "Thirza Ahmad Tsaqif",
        "Class": "PBP E",
        "Inventory" : [
            {"name": "Boeing 737 - 900",
             "amount": "10",
             "description": "Pesawat Komersial Boeing 737 - 900 yang diluncurkan pada tahun 1997",
             "engine": "Jet",
             "winglet": "True"
             },
            {"name": "Boeing 747 - 400",
             "amount": "10",
             "description": "Pesawat Komersial Boeing 747 - 400 yang diluncurkan pada tahun 1988",
             "engine": "Jet",
             "winglet": "False"
             },
             {"name": "ATR 42 - 400",
              "amount": "50",
              "description": "Pesawat Komersial ATR 42 - 400 yang diluncurkan pada tahun 1981",
              "engine": "Propeller",
              "winglet": "False"
              }
        ]
    }
    return render(request, "main.html", context)