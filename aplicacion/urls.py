from django.urls import path

from aplicacion import views

urlpatterns = [
    path('aplicacion/', views.aplicacion,name="aplicacion"),
]