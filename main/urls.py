from django.urls import path

from . import views

app_name = 'main'

urlpatterns = [
    path('', views.home, name='home'),
    path('objects/', views.objects, name='objects'),
    path('detail/<int:estate_id>/', views.detail, name='detail'),
    path('team/', views.team, name='team'),
    path('add_object/', views.add_object, name='add_object'),
    path('add_realtor/', views.add_realtor, name='add_realtor'),
]
