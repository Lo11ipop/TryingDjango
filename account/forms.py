from django import forms
from .models import *


class PatientForm(forms.ModelForm):

    class Meta:
        model = Patient
        exclude = ['Login', 'BloodType']


class AddressForm(forms.ModelForm):

    class Meta:
        model = Address
        exclude = ['Login']


class MedCardForm(forms.ModelForm):

    class Meta:
        model = MedCard
        exclude = ['Login']


class PatientHistoryForm(forms.ModelForm):

    class Meta:
        model = Patienthistory
        exclude = ['Login']


class PatientAlergikForm(forms.ModelForm):

    class Meta:
        model = Alergik
        exclude = ['PatientName']


class PatientOperationForm(forms.ModelForm):
    class Meta:
        model = Operation
        exclude = ['PatientName']


class PatientGraftForm(forms.ModelForm):
    class Meta:
        model = Graft
        exclude = ['PatientName']


class PatientChronikForm(forms.ModelForm):
    class Meta:
        model = Chronicdisease
        exclude = ['PatientName']
