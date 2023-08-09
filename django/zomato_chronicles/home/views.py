from django.shortcuts import render
from .db_utils import read_data, write_data
from django.http import HttpResponse
# Create your views here.

def get_menu():
   menu,_ = read_data()
   return menu

def read_dish(request):
   menu = get_menu()
   return render(request, "home.html", {"menu": menu})
    


  

 
  