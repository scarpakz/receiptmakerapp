# Generated by Django 5.1.4 on 2024-12-22 02:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='receiptmodel',
            name='total',
            field=models.FloatField(default=0, max_length=100),
        ),
    ]
