# Generated by Django 2.1.3 on 2018-11-14 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mail', '0010_auto_20181114_2308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recruit',
            name='img',
            field=models.FileField(blank=True, null=True, upload_to='', verbose_name='이미지'),
        ),
    ]
