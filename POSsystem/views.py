from django.http import HttpRequest,HttpResponse,request
from django.shortcuts import render
def home(request):
    # return HttpResponse("Hello")
    return render(request,'Home/index.html')

def item_entry(request):
    return render(request,'item_entry/index.html') 

def add_item(request):
    return render(request,'item_entry/additem.html')