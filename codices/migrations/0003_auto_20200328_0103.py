# Generated by Django 2.2.8 on 2020-03-28 01:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('codices', '0002_auto_20200322_1944'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curso',
            name='imagen',
            field=models.ImageField(upload_to='cursos/'),
        ),
    ]
