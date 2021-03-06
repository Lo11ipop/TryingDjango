# Generated by Django 2.0.6 on 2018-06-12 11:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dict', '0004_auto_20180612_1242'),
        ('account', '0003_alergik_chronicdisease_operation'),
    ]

    operations = [
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id_schedule', models.AutoField(primary_key=True, serialize=False)),
                ('TimeSince', models.TimeField()),
                ('TimeFor', models.TimeField()),
                ('DoctorName', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='account.Doctor')),
                ('WeekDay', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='dict.Days')),
            ],
            options={
                'db_table': 't_schedule',
            },
        ),
    ]
