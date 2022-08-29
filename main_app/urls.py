from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('houses/', views.houses_index, name='index'),
    path('houses/<int:house_id>/', views.houses_detail, name='detail'),
    path('houses/create/', views.HouseCreate.as_view(), name='houses_create'),
]