from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from account.models import *
from .models import *
from .forms import *
from dict.models import *
from account.forms import *


def patientinfo(request, pat):

    PH = Patienthistory.objects.filter(Login=User.objects.get(username=pat)).all()
    PA = Alergik.objects.filter(PatientName__Login=User.objects.get(username=pat)).all()
    PO = Operation.objects.filter(PatientName__Login=User.objects.get(username=pat)).all()
    PG = Graft.objects.filter(PatientName__Login=User.objects.get(username=pat)).all()
    PC = Chronicdisease.objects.filter(PatientName__Login=User.objects.get(username=pat)).all()
    return render(request, 'doctors/patientinfo.html', {'PH': PH, 'PA': PA, 'PO': PO, 'PG': PG, 'PC': PC, 'pat': pat})


def newhistory(request, pat):

    if request.POST:
        PH = PatientHistoryForm(request.POST)
        if PH.is_valid():
            instance = PH.save(commit=False)
            instance.Login = User.objects.get(username=pat)
            instance.save()
            return redirect('information_patient', pat=pat)
    PH = PatientHistoryForm()
    return render(request, 'doctors/newhistory.html', {'PH': PH, 'pat': pat})


def newalergik(request, pat):

    if request.POST:
        PA = PatientAlergikForm(request.POST)
        if PA.is_valid():
            instance = PA.save(commit=False)
            instance.PatientName = Patient.objects.get(Login=User.objects.get(username=pat))
            instance.save()
            return redirect('information_patient', pat=pat)
    PA = PatientAlergikForm()
    return render(request, 'doctors/newalergik.html', {'PA': PA, 'pat': pat})


def newoperation(request, pat):

    if request.POST:
        PO = PatientOperationForm(request.POST)
        if PO.is_valid():
            instance = PO.save(commit=False)
            instance.PatientName = Patient.objects.get(Login=User.objects.get(username=pat))
            instance.save()
            return redirect('information_patient', pat=pat)
    PO = PatientOperationForm()
    return render(request, 'doctors/newoperation.html', {'PO': PO, 'pat': pat})


def newgraft(request, pat):

    if request.POST:
        PG = PatientGraftForm(request.POST)
        if PG.is_valid():
            instance = PG.save(commit=False)
            instance.PatientName = Patient.objects.get(Login=User.objects.get(username=pat))
            instance.save()
            return redirect('information_patient', pat=pat)
    PG = PatientGraftForm()
    return render(request, 'doctors/newgraft.html', {'PG': PG, 'pat': pat})


def newchronik(request, pat):

    if request.POST:
        PC = PatientChronikForm(request.POST)
        if PC.is_valid():
            instance = PC.save(commit=False)
            instance.PatientName = Patient.objects.get(Login=User.objects.get(username=pat))
            instance.save()
            return redirect('information_patient', pat=pat)
    PC = PatientChronikForm()
    return render(request, 'doctors/newchronik.html', {'PC': PC, 'pat': pat})


@login_required(login_url='login')
def reception(request):

    doctors = Doctor.objects.all()
    receip = ReceptionForm()
    days = Days.objects.all()
    return render(request, 'other/reception.html', {'doctors': doctors, 'receip': receip, 'days': days})


def receptioninfo(request, id_d):

    if request.POST:
        receip = ReceptionForm(request.POST)
        if receip.is_valid():
            instance = receip.save(commit=False)
            instance.Doctor = Doctor.objects.get(id_d=id_d)
            instance.Patient = Patient.objects.get(Login=request.user)
            instance.save()
    return render(request, 'other/receptioninfo.html', {'form': instance})
