# Generated by Django 2.1.3 on 2018-11-14 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mail', '0005_auto_20181114_2142'),
    ]

    operations = [
        migrations.AddField(
            model_name='recruit',
            name='url',
            field=models.URLField(blank=True, null=True, verbose_name='공고주소'),
        ),
    ]
