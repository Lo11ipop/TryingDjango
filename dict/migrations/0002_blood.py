# Generated by Django 2.0.6 on 2018-06-12 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dict', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blood',
            fields=[
                ('id_blood', models.AutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 't_blood',
            },
        ),
    ]
