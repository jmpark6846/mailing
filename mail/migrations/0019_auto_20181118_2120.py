# Generated by Django 2.1.3 on 2018-11-18 12:20

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('mail', '0018_recruit__materials'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recruit',
            name='duedate',
            field=models.CharField(default=django.utils.timezone.now, max_length=10, verbose_name='마감일'),
            preserve_default=False,
        ),
    ]
