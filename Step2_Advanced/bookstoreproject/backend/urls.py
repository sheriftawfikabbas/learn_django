from django.urls import path
import backend.views as views

urlpatterns = [
    path('', views.index,name='index')
]