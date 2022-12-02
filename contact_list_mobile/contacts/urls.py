from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('new/', views.add_contact, name='new'),
    path('details/<str:pk>/', views.contact_details, name='details'),
    path('update/<str:pk>/', views.contact_update, name='update')
]
