from django import forms
from .models import *
from account.models import *


class DoctorForm(forms.ModelForm):

    class Meta:
        model = Doctor
        exclude = ['Specialty', 'Login']


class ReceptionForm(forms.ModelForm):

    class Meta:
        model = Reception
        exclude = ['Doctor', 'Patient']

