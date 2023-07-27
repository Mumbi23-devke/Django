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


def delete(request, id):
    d = People.objects.get(id=id)
    d.delete()
    return redirect("/")
    return render(request, "index.html")


def updateData(request, id):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        age = request.POST.get('age')
        gender = request.POST.get('gender')

        edit_data = People.objects.get(id=id)
        edit_data.name = name
        edit_data.email = email
        edit_data.age = age
        edit_data.gender = gender
        edit_data.save()

        return redirect("/")

    dta = People.objects.get(id=id)
    context = {"dta": dta}
    return render(request, "edit.html", context)
