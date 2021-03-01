from . import views
from django.urls import path

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:name>", views.greet, name="greet"),
    path("woosal", views.woosal, name="woosal"),
    path("chalabi", views.chalabi, name="chalabi")
]
