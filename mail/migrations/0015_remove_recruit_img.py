# Generated by Django 2.1.3 on 2018-11-18 10:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mail', '0014_company_logo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recruit',
            name='img',
        ),
    ]
