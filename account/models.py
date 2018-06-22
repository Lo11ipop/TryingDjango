from django.db import models
from django.contrib.auth.models import User
from dict.models import Blood, Days


class Doctorspec(models.Model):
    id_doct_spec = models.AutoField(primary_key=True)
    Specialty = models.CharField(max_length=30)
    Description = models.TextField(default='')

    class Meta:
        db_table = 't_doct_spec'

    def __str__(self):
        return self.Specialty


class Patient(models.Model):
    id_p = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=20)
    Patronymic = models.CharField(max_length=20)
    Surname = models.CharField(max_length=20)
    Phone = models.CharField(max_length=20)
    Email = models.CharField(max_length=30)
    Login = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    BloodType = models.ForeignKey(Blood, default=None, on_delete=models.CASCADE)

    class Meta:
        db_table = 't_patient'

    def __str__(self):
        return self.Name+'_'+self.Surname


class Doctor(models.Model):
    id_d = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=20)
    Patronymic = models.CharField(max_length=20)
    Surname = models.CharField(max_length=20)
    Phone = models.CharField(max_length=15)
    Email = models.CharField(max_length=30)
    Photo = models.ImageField(default='default.png', blank=True)
    Login = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    Specialty = models.ForeignKey(Doctorspec, default=None, on_delete=models.CASCADE)

    class Meta:
        db_table = 't_doctor'

    def __str__(self):
        return self.Name+'_'+self.Surname


class MedCard(models.Model):
    id_mc = models.AutoField(primary_key=True)
    Birthday = models.DateField()
    Work_Place = models.CharField(max_length=100)
    Position = models.CharField(max_length=100)
    Receipt_Date = models.DateField()
    Login = models.ForeignKey(User, default=None, on_delete=models.CASCADE)

    class Meta:
        db_table = 't_med_card'


class Address(models.Model):
    id_a = models.AutoField(primary_key=True)
    Town_Index = models.IntegerField()
    Locality = models.CharField(max_length=30)
    Post_Number = models.IntegerField()
    Region = models.CharField(max_length=30)
    Street = models.CharField(max_length=30)
    House = models.IntegerField()
    Apart_Number = models.IntegerField()
    Login = models.ForeignKey(User, default=None, on_delete=models.CASCADE)

    class Meta:
        db_table = 't_address'


class Graft(models.Model):
    id_graft = models.AutoField(primary_key=True)
    Date = models.DateField()
    Name = models.CharField(max_length=30)
    PatientName = models.ForeignKey(Patient, default=None, on_delete=models.CASCADE)

    class Meta:
        db_table = 't_graft'

    def __str__(self):
        return self.Date.__str__() + "_" + self.Name


class Alergik(models.Model):
    id_alergik = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=30)
    PatientName = models.ForeignKey(Patient, default=None, on_delete=models.CASCADE)

    class Meta:
        db_table = 't_alergik'

    def __str__(self):
        return self.Name + "_" + self.PatientName.Surname + "_" + self.PatientName.Name


class Operation(models.Model):
    id_operation = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=30)
    Description = models.TextField(default=None)
    PatientName = models.ForeignKey(Patient, default=None, on_delete=models.CASCADE)

    class Meta:
        db_table = 't_operation'

    def __str__(self):
        return self.Name + "_" + self.PatientName.Surname + "_" + self.PatientName.Name


class Chronicdisease(models.Model):
    id_chronic_disease = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=30)
    PatientName = models.ForeignKey(Patient, default=None, on_delete=models.CASCADE)

    class Meta:
        db_table = 't_chronic_disease'

    def __str__(self):
        return self.Name + "_" + self.PatientName.Surname + "_" + self.PatientName.Name


class Schedule(models.Model):
    id_schedule = models.AutoField(primary_key=True)
    DoctorName = models.ForeignKey(Doctor, default=None, on_delete=models.CASCADE)
    WeekDay = models.ForeignKey(Days, default=None, on_delete=models.CASCADE)
    TimeSince = models.TimeField()
    TimeFor = models.TimeField()

    class Meta:
        db_table = 't_schedule'

    def __str__(self):
        return self.WeekDay.Name + "_" + self.DoctorName.Surname + "_" + self.DoctorName.Name


class Patienthistory(models.Model):
    id_history = models.AutoField(primary_key=True)
    Diag = models.CharField(max_length=100)
    Epicris = models.TextField(default=None)
    Login = models.ForeignKey(User, default=None, on_delete=models.CASCADE)

    class Meta:
        db_table = 't_history'

    def __str__(self):
        return self.Diag + "_" + Patient.objects.get(Login=self.Login).Surname
