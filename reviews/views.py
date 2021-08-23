from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# def index(request):
#     name = request.GET.get('name') or "aBookr"
#
#     return HttpResponse(f"{name} book site")

def index(request):
    name="mike"
    context = { "name" : name}

    return render(request,'base.html', context)

def search(request):

    search_text = request.GET.get('search_text',"")
    context = {"search_text": search_text}
    return render(request,'search.html', context)

