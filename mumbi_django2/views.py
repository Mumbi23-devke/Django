from django.shortcuts import render, redirect
from .models import People


def aboutpage(request):
    return render(request, "About.html")


def servpage(request):
    return render(request, "Services.html")


def blogpage(request):
    return render(request, "Blog.html")


def projpage(request):
    return render(request, "Project.html")


def indexpage(request):
    data = People.objects.all()
    context = {"data": data}
    return render(request, "index.html", context)


def signup(request):
    return render(request, "Signup.html")


def home(request):
    return render(request, "homepage.html")


def insertdata(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        age = request.POST.get('age')
        gender = request.POST.get('gender')

        query = People.objects.create(name=name, email=email, age=age, gender=gender)
        query.save()
        return redirect("/")
    return render(request, "index.html")
