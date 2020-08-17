from django.shortcuts import render, HttpResponse

# Create your views here.

def home_page(request):
    # return HttpResponse('<html> <title>To-Do lists</title> <h1>To-Do</h1> </html>')
    if request.method == 'POST':
        # print(request.POST)
        # return HttpResponse(request.POST['item_text'])
        context_dict = {
            'new_item_text': request.POST['item_text']
        }
        return render(request, 'home.html', context=context_dict)
    return render(request, 'home.html')