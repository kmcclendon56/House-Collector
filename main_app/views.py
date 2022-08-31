from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import House
from .forms import LocationForm


def home(request):
    return HttpResponse('<h1>Welcome to the House Collector</h1>')

def about(request):
    return render(request, 'about.html')

def houses_index(request):
    houses = House.objects.all()
    return render(request, 'houses/index.html', { 'houses': houses })

def houses_detail(request, house_id):
    house = House.objects.get(id=house_id)
    location_form = LocationForm()
    return render(request, 'houses/detail.html', {
        'house': house, 'location_form': location_form
        })

def add_location(request, house_id):
    form = LocationForm(request.POST)
    if form.is_valid():
        new_location = form.save(commit=False)
        new_location.house_id = house_id
        new_location.save()
    return redirect('detail', house_id=house_id)

class HouseCreate(CreateView):
    model = House
    fields = '__all__'

class HouseUpdate(UpdateView):
  model = House
  fields = ['rooms_baths', 'sqft', 'gas_stove', 'notes', 'allows_dogs']

class HouseDelete(DeleteView):
  model = House
  success_url = '/houses/'