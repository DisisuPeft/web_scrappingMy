# Generated by Django 5.1.2 on 2024-11-09 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_alter_usercustomize_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usercustomize',
            name='perfilId',
            field=models.IntegerField(default=None, null=True),
        ),
    ]
