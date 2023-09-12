from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'appname': 'Inventory Manager',
        'name': 'Muhammad Nabiel Subhan',
        'class': 'PBP A'
    }

    return render(request, "main.html", context)