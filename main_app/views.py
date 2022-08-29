from django.shortcuts import render
from django.http import HttpResponse
from .models import House





def home(request):
  return HttpResponse('<h1>Welcome to the House Collector</h1>')

def about(request):
    return render(request, 'about.html')

def houses_index(request):
  return render(request, 'houses/index.html', { 'houses': houses })

def house_details(request, house_id):
    house = House.objects.get(id=house_id)
    return render(request, 'house/detail.html', {'house': house})