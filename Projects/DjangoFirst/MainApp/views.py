from django.shortcuts import render, HttpResponse, Http404
from MainApp import models
from MainApp.models import Item

name = "Виталий"
patronymic = "Витальевич"
surname = "Барышев"
full_name = "Барышев В.В."
phone = "8 - 910 - 396 - 37 - 26"
email = "baryshev_vv@vsw.ru"
"""
items = [
    {"id": 1, "name": "Кроссовки abibas", "quantity": 5},
    {"id": 2, "name": "Куртка кожаная", "quantity": 2},
    {"id": 3, "name": "Coca-cola 1 литр", "quantity": 12},
    {"id": 4, "name": "Картофель фри", "quantity": 0},
    {"id": 5, "name": "Кепка", "quantity": 124},
]
"""

def home(request):
    return render(request, "index.html")


def about(request):
    context = {
        "name": name,
        "patronymic": patronymic,
        "surname": surname,
        "full_name": full_name,
        "phone": phone,
        "email": email,
    }
    return render(request, "about.html", context)


def item_list(request):
    items = Item()
    context = {
        "items": items
    }
    return render(request, "item_list.html", context)


def item_page(request, id):
    for item in items:
        if item["id"] == id:
            return render(request, "item_page.html", item)
    raise Http404(request)
