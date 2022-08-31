from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('houses/', views.houses_index, name='index'),
    path('houses/<int:house_id>/', views.houses_detail, name='detail'),
    path('houses/create/', views.HouseCreate.as_view(), name='houses_create'),
    path('houses/<int:pk>/update/', views.HouseUpdate.as_view(), name='houses_update'),
    path('houses/<int:pk>/delete/', views.HouseDelete.as_view(), name='houses_delete'),
    path('houses/<int:house_id>/add_location/', views.add_location, name='add_location'),
]