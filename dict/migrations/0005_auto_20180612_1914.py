# Generated by Django 2.0.6 on 2018-06-12 16:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dict', '0004_auto_20180612_1242'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Disease',
        ),
        migrations.DeleteModel(
            name='Medicine',
        ),
        migrations.DeleteModel(
            name='Procedure',
        ),
    ]