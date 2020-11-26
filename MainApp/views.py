from django.shortcuts import render, HttpResponse, Http404
from .models import Item
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.
user_data = {
    "surname": "Левина",
    "name": "Ксения",
    "second_name": "Евгеньевна",
}
items = [
   {"id": 1, "name": "Кроссовки abibas"},
   {"id": 2, "name": "Куртка кожаная"},
   {"id": 3, "name": "Coca-cola 1 литр"},
   {"id": 4, "name": "Картофель фри"},
   {"id": 5, "name": "Кепка"},
]

#def main(request):
#    text = f"""
#    <h1> "Изучаем django" </h1>
#    <strong>Автор</strong>:<i>
#    {user_data['surname']} {user_data['name'][0]}.{user_data['second_name'][0]}.</i>
#    """
#    return HttpResponse(text)

def main(request):

    return render(request, 'index.html', context=user_data)

#def item(request, id):
#    context = {}
#    for item in items:
#        if item["id"] == id:
#            context["item"] = item
#            return render(request, "item.html", context)
#    raise Http404

#def item2(request):
#    for item in items:
#        if item["id"] == 2:
#            return HttpResponse(item["name"])

def item_list(request):
    items = Item.objects.all()
    context = {"items": items}
    return render(request, "items_list.html", context)

def item(request, id):
        context = {}
        try:
            Item.objects.get(id=id)
        except ObjectDoesNotExist:
            raise Http404
        context["item"] = item
        return render(request, "item.html", context)