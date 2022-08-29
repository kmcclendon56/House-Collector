from django.shortcuts import render
from django.http import HttpResponse
from .models import House
from django.views.generic.edit import CreateView





def home(request):
    return HttpResponse('<h1>Welcome to the House Collector</h1>')

def about(request):
    return render(request, 'about.html')

def houses_index(request):
    houses = House.objects.all()
    return render(request, 'houses/index.html', { 'houses': houses })

def houses_detail(request, house_id):
    house = House.objects.get(id=house_id)
    return render(request, 'houses/detail.html', {'house': house})

class HouseCreate(CreateView):
    model = House
    fields = '__all__'