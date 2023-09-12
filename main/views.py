from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'appname': 'inventory-manager',
        'name': 'Muhammad Nabiel Subhan',
        'class': 'PBP A'
    }

    return render(request, "main.html", context)