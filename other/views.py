from .models import *
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render
from account.views import *


def news(request, slug):

    doctors = Doctor.objects.all()
    article = Article.objects.get(slug=slug)
    if request.user.is_authenticated:
        for doctor in doctors:
            if request.user == doctor.Login:
                return render(request, 'doctors/news.html', {'article': article})
    return render(request, 'other/news.html', {'article': article})
