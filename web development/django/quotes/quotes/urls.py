from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_quotes, name='show_quotes')
]