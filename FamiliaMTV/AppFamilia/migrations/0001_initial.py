# Generated by Django 4.1 on 2022-09-05 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Familia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=56)),
                ('apellido', models.CharField(max_length=50)),
                ('Edad', models.IntegerField()),
                ('relacion', models.CharField(max_length=50)),
                ('cumple', models.DateField()),
            ],
        ),
    ]