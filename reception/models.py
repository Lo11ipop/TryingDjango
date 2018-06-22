from django.db import models
from account.models import *


class Reception(models.Model):
    id_r = models.AutoField(primary_key=True)
    Doctor = models.ForeignKey(Doctor, default=None, on_delete=models.CASCADE)
    Patient = models.ForeignKey(Patient, default=None, on_delete=models.CASCADE)
    Date = models.DateField()

    class Meta:
        db_table = 't_reception'

    def __str__(self):
        return self.Date.__str__() + "_" + self.Doctor.Surname + "_" + self.Patient.Surname
