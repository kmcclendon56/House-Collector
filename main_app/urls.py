from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('houses/', views.houses_index, name='index'),
    path('houses/<int:house_id>/', views.houses_detail, name='detail'),
    path('houses/create/', views.HouseCreate.as_view(), name='houses_create'),
    path('houses/<int:pk>/update/',
         views.HouseUpdate.as_view(), name='houses_update'),
    path('houses/<int:pk>/delete/',
         views.HouseDelete.as_view(), name='houses_delete'),
    path('houses/<int:house_id>/add_location/',
         views.add_location, name='add_location'),
    path('houses/<int:house_id>/assoc_feature/<int:feature_id>/',
         views.assoc_feature, name='assoc_feature'),
    path('features/', views.FeatureList.as_view(), name='features_index'),
    path('features/<int:pk>/', views.FeatureDetail.as_view(), name='features_detail'),
    path('features/create/', views.FeatureCreate.as_view(), name='features_create'),
    path('features/<int:pk>/update/',
         views.FeatureUpdate.as_view(), name='features_update'),
    path('features/<int:pk>/delete/',
         views.FeatureDelete.as_view(), name='features_delete'),
]
