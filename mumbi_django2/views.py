from django.shortcuts import render, redirect


def aboutpage(request):
    return render(request, "About.html")


def servpage(request):
    return render(request, "Services.html")


def blogpage(request):
    return render(request, "Blog.html")


def projpage(request):
    return render(request, "Project.html")
