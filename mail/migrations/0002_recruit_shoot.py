# Generated by Django 2.1.3 on 2018-11-14 09:57

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('mail', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='recruit',
            name='shoot',
            field=models.DateField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='발송일'),
        ),
    ]
