# Generated by Django 2.1.3 on 2018-11-18 11:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mail', '0015_remove_recruit_img'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recruit',
            name='_link',
        ),
    ]
