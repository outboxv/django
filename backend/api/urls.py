from django.urls import path
from . import views

urlpatterns = [
    path("",views.getStores),
    path("add/",views.addStore),
]
