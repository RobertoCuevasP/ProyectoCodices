# Generated by Django 2.2.8 on 2020-03-30 00:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('codices', '0008_auto_20200330_0003'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='perfil',
            name='CI',
        ),
        migrations.RemoveField(
            model_name='perfil',
            name='fechaNacimiento',
        ),
        migrations.RemoveField(
            model_name='perfil',
            name='telefono',
        ),
    ]
