from django.shortcuts import render, redirect
from .models import Student
from .models import Teacher


def aboutpage(request):
    return render(request, "About.html")


def servpage(request):
    return render(request, "Services.html")


def blogpage(request):
    return render(request, "Blog.html")


def projpage(request):
    return render(request, "Project.html")


def indexpage(request):
    return render(request, "index.html")


def signup(request):
    return render(request, "Signup.html")


def home(request):
    return render(request, "homepage.html")


def insertdata(request):
    if request.method == "POST":
        fullname = request.POST.get('fullname')
        email_address = request.POST.get('email_address')
        age = request.POST.get('age')
        phone_number = request.POST.get('phone_number')
        password = request.POST.get('password')

        query = Student(fullname=fullname, email_address=email_address, age=age, phone_number=phone_number, password=password)
        query.save()
        return redirect("/")
