# Generated by Django 2.1.3 on 2018-11-14 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recruit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(max_length=255, verbose_name='회사명')),
                ('field', models.CharField(max_length=255, verbose_name='모집 분야')),
                ('duedate', models.DateField(blank=True, null=True, verbose_name='마감일')),
                ('place', models.CharField(max_length=255, verbose_name='근무지')),
                ('career', models.CharField(max_length=255, verbose_name='경력 구분')),
                ('detail', models.CharField(max_length=255, verbose_name='특이사항')),
            ],
        ),
    ]