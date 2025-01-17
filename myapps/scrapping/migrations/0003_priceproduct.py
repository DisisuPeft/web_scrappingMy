# Generated by Django 5.1.2 on 2024-11-10 04:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scrapping', '0002_alter_urls_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='PriceProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('URLs_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='prices', to='scrapping.urls')),
            ],
        ),
    ]
