# Generated by Django 3.0 on 2022-10-07 16:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lettings', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='address',
            table='oc_lettings_site_Address',
        ),
        migrations.AlterModelTable(
            name='letting',
            table='oc_lettings_site_Letting',
        ),
    ]
