# Generated by Django 2.0.6 on 2018-06-12 08:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id_a', models.AutoField(primary_key=True, serialize=False)),
                ('Town_Index', models.IntegerField()),
                ('Locality', models.CharField(max_length=30)),
                ('Post_Number', models.IntegerField()),
                ('Region', models.CharField(max_length=30)),
                ('Street', models.CharField(max_length=30)),
                ('House', models.IntegerField()),
                ('Apart_Number', models.IntegerField()),
                ('Login', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 't_address',
            },
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id_d', models.AutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=20)),
                ('Patronymic', models.CharField(max_length=20)),
                ('Surname', models.CharField(max_length=20)),
                ('Phone', models.CharField(max_length=15)),
                ('Email', models.CharField(max_length=30)),
                ('Photo', models.ImageField(blank=True, default='default.png', upload_to='')),
            ],
            options={
                'db_table': 't_doctor',
            },
        ),
        migrations.CreateModel(
            name='Doctorspec',
            fields=[
                ('id_doct_spec', models.AutoField(primary_key=True, serialize=False)),
                ('Specialty', models.CharField(max_length=30)),
                ('Description', models.TextField(default='')),
            ],
            options={
                'db_table': 't_doct_spec',
            },
        ),
        migrations.CreateModel(
            name='MedCard',
            fields=[
                ('id_mc', models.AutoField(primary_key=True, serialize=False)),
                ('Birthday', models.DateField()),
                ('Work_Place', models.CharField(max_length=100)),
                ('Position', models.CharField(max_length=100)),
                ('Receipt_Date', models.DateField()),
                ('Login', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 't_med_card',
            },
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id_p', models.AutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=20)),
                ('Patronymic', models.CharField(max_length=20)),
                ('Surname', models.CharField(max_length=20)),
                ('Phone', models.CharField(max_length=20)),
                ('Email', models.CharField(max_length=30)),
                ('Login', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 't_patient',
            },
        ),
        migrations.AddField(
            model_name='doctor',
            name='Specialty',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='account.Doctorspec'),
        ),
    ]