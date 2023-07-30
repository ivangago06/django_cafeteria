from django.shortcuts import render,  HttpResponse

# Create your views here.
def home(request):
    return render(request,"cafeteria_app/home.html")

def about(request):
    return render(request,"cafeteria_app/about.html")

def history(request):
    return render(request,"cafeteria_app/history.html")

def services(request):
    return render(request,"cafeteria_app/services.html")

def blog(request):
    return render(request,"cafeteria_app/blog.html")

def contact(request):
    return render(request,"cafeteria_app/contact.html")