# Generated by Django 5.1.2 on 2024-11-09 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usercustomize',
            name='password',
            field=models.CharField(max_length=128, verbose_name='password'),
        ),
    ]
