from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from account.views import *
from other.models import *
from account.models import *
from reception.models import *
from django.http import HttpResponse
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reception.forms import *
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import inch, cm, mm
import re


def homepage(request):

    doctors = Doctor.objects.all()
    articles = Article.objects.all()
    if request.user.is_authenticated:
        for doctor in doctors:
            if request.user == doctor.Login:
                return render(request, 'doctors/home.html', {'articles': articles})
    return render(request, 'other/home.html', {'articles': articles})


def reform(request):

    doctors = Doctor.objects.all()
    if request.user.is_authenticated:
        for doctor in doctors:
            if request.user == doctor.Login:
                return render(request, 'doctors/reform.html')
    return render(request, 'other/reform.html')


def contact(request):

    doctors = Doctor.objects.all()
    if request.user.is_authenticated:
        for doctor in doctors:
            if request.user == doctor.Login:
                return render(request, 'doctors/contact.html')
    return render(request, 'other/contact.html')


def inforamtion(request):

    medcard = MedCard.objects.get(Login=request.user)
    address = Address.objects.get(Login=request.user)
    patient = Patient.objects.get(Login=request.user)
    return render(request, 'other/cabinet.html', {'address': address, 'patient': patient, 'medcard': medcard})


def myqueue(request):

    recs = Reception.objects.filter(Patient__Login=request.user).all()
    return render(request, 'other/queue.html', {'recs': recs})


def muqueuedownload(request, rec):

    pdfmetrics.registerFont(TTFont('FreeSans', 'FreeSans.ttf'))
    width, height = A4
    response = HttpResponse(content_type='application/pdf;')
    response['Content-Disposition'] = 'attachment; filename="Queue.pdf"'
    if request.POST:
        receip = Reception.objects.get(id_r=rec)
        dr = canvas.Canvas(response, pagesize=A4)
        dr.setFont('FreeSans', 16)
        dr.drawString(30*mm, height-20*mm, 'ЛІКАР:')
        dr.drawString(110*mm, height-20*mm, 'ПАЦІЄНТ:')
        dr.setFont('FreeSans', 14)
        dr.drawString(30*mm, height-30*mm, "Ім'я: " + receip.Doctor.Name)
        dr.drawString(30 * mm, height - 35 * mm, "По батькові: " + receip.Doctor.Patronymic)
        dr.drawString(30 * mm, height - 40 * mm, "Прізвище: " + receip.Doctor.Surname)
        dr.drawString(30 * mm, height - 45 * mm, "Спеціальність: " + receip.Doctor.Specialty)
        dr.drawString(110 * mm, height - 30 * mm, "Ім'я: " + receip.Patient.Name)
        dr.drawString(110 * mm, height - 35 * mm, "По батькові: " + receip.Patient.Patronymic)
        dr.drawString(110 * mm, height - 40 * mm, "Прізвище: " + receip.Patient.Surname)
        dr.drawString(30 * mm, height - 60 * mm, "Дата прийому: " + receip.Date.__str__())
        dr.showPage()
        dr.save()
    return response


def doctros_list(request):

    doctors = Doctor.objects.all()
    return render(request, 'other/doctors_list.html', {'doctors': doctors})


def patient_list(request):

    receip = Reception.objects.filter(Doctor__Login=request.user)
    return render(request, 'doctors/patient.html', {'receips': receip})


