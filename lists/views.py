from django.shortcuts import render, HttpResponse, redirect
from lists.models import Item

# Create your views here.

def home_page(request):
    if request.method == 'POST':
        Item.objects.create(text=request.POST['item_text'])
        return redirect('/')
    qs = Item.objects.all()
    return render(request, 'home.html', {'items' : qs})