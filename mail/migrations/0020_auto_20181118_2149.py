# Generated by Django 2.1.3 on 2018-11-18 12:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mail', '0019_auto_20181118_2120'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recruit',
            old_name='_materials',
            new_name='material_text',
        ),
    ]
