from django.db import models


class Days(models.Model):
    id_day = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=20)

    class Meta:
        db_table = 't_week_days'

    def __str__(self):
        return self.Name


class Blood(models.Model):
    id_blood = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=20)

    class Meta:
        db_table = 't_blood'

    def __str__(self):
        return self.Name


