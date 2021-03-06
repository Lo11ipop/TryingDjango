# Generated by Django 2.0.6 on 2018-06-12 09:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dict', '0004_auto_20180612_1242'),
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Graft',
            fields=[
                ('id_graft', models.AutoField(primary_key=True, serialize=False)),
                ('Date', models.DateField()),
                ('Name', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 't_graft',
            },
        ),
        migrations.AddField(
            model_name='patient',
            name='BloodType',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='dict.Blood'),
        ),
        migrations.AddField(
            model_name='graft',
            name='PatientName',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='account.Patient'),
        ),
    ]
