from django.shortcuts import render, get_object_or_404, redirect


def home_view(request):
    return render(request, 'home/home.html')