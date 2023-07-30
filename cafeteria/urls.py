from django.contrib import admin
from django.urls import path, include 

from cafeteria_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home,name="home"),
    path('about/', views.about,name="about"),
    path('history/', views.history,name="history"),
    path('services/', views.services,name="services"),
    path('blog/', views.blog,name="blog"),
    path('contact/', views.contact,name="contact"), 
    path('', include('aplicacion.urls')),
    path('', include('contacto.urls')),
]
