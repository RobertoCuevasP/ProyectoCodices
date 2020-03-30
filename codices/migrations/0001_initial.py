# Generated by Django 2.2.8 on 2020-03-22 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('categoria', models.CharField(choices=[('Deportes', 'Deportes'), ('Tecnología', 'Tecnología'), ('Arte', 'Arte'), ('Educación', 'Educación')], max_length=10)),
                ('costo', models.CharField(max_length=10)),
                ('tipo', models.BooleanField()),
                ('descripcion', models.CharField(max_length=1000)),
                ('fechaInicio', models.DateField()),
                ('fechaFin', models.DateField()),
                ('imagen', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Instructor',
            fields=[
                ('nombre', models.CharField(max_length=100)),
                ('CI', models.IntegerField()),
                ('ID', models.AutoField(primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=254)),
                ('telefono', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Supervisor',
            fields=[
                ('nombre', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=254)),
                ('telefono', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False)),
                ('CI', models.IntegerField()),
                ('nombre', models.CharField(max_length=100)),
                ('telefono', models.IntegerField()),
                ('fechaNacimiento', models.DateField()),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
