# Generated by Django 2.0.6 on 2018-06-12 18:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_auto_20180612_2118'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patienthistory',
            name='Login',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
