from django.urls import path

from . import views

urlpatterns = [
    path('create_view', views.create_view, name='create-view'),
]