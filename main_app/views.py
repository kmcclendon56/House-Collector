from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import House, Feature
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
    features_house_doesnt_have = Feature.objects.exclude(id__in = house.features.all().values_list('id'))
    location_form = LocationForm()
    return render(request, 'houses/detail.html', {
        'house': house, 'location_form': location_form, 'features': features_house_doesnt_have
        })

def assoc_feature(request, house_id, feature_id):
  House.objects.get(id=house_id).features.add(features_id)
  return redirect('detail', house_id=house_id)

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

class FeatureList(ListView):
    model = Feature

class FeatureDetail(DetailView):
    model = Feature

class FeatureCreate(CreateView):
    model = Feature
    fields = '__all__'

class FeatureUpdate(UpdateView):
    model = Feature
    fields = ['name']

class FeatureDelete(DeleteView):
    model = Feature
    success_url = '/features/'