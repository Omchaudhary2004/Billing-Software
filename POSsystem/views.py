from django.http import HttpRequest,HttpResponse,request
from django.shortcuts import render
from Data_controll.Creator_file import item_en
from random import randint
from django.http import JsonResponse
from django.views.generic import View


def home(request):
    # return HttpResponse("Hello")
    return render(request,'Home/index.html')

def item_entry(request):
    # item_data = item_en() #### ,{'item_data:':item_data}
    return render(request,'item_entry/index.html') 

def add_item(request):
    return render(request,'item_entry/additem.html')

# def test(request):
#     def get(self , request):
#         number = randint(1, 10)
#         return JsonResponse({'number':number})
#     .

class tests(View):
    def get(self , request):
        if request.headers.get('X-Requested-With') == 'XMLHttpResquest':
            number = randint(1, 10)
            return JsonResponse({'number':number})
        return render(request,'index.html')