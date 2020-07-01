from django.contrib import admin
from django.urls import path, include
from .views import apiView, serialView

urlpatterns = [
    path('1', apiView), 
    path('serialize', serialView),
]
