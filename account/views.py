from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from account.forms import *


def registration(request):
    if request.POST:
        user = UserCreationForm(request.POST)
        patient = PatientForm(request.POST)
        address = AddressForm(request.POST)
        medcard = MedCardForm(request.POST)
        print(request.POST)
        if user.is_valid():
            if user.is_valid() and address.is_valid() and medcard.is_valid() and patient.is_valid():
                 us = user.save()
                 login(request, us)
                 instanceaddress = address.save(commit=False)
                 instanceaddress.Login = request.user
                 instanceaddress.save()
                 instancemedcard = medcard.save(commit=False)
                 instancemedcard.Login = request.user
                 instancemedcard.save()
                 instancepatient = patient.save(commit=False)
                 instancepatient.Login = request.user
                 instancepatient.save()
                 return redirect('homepage')
    else:
        user = UserCreationForm()
        patient = PatientForm()
        address = AddressForm()
        medcard = MedCardForm()
    return render(request, 'other/registration.html', {'user': user, 'patient': patient, 'address': address, 'medcard': medcard})


def login_view(request):
    if request.POST:
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('homepage')
    else:
        form = AuthenticationForm()
    return render(request, 'other/login.html', {'form': form})


def logout_view(request):
    if request.POST:
        logout(request)
    return redirect('homepage')
