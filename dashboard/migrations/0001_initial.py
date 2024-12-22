# Generated by Django 5.1.4 on 2024-12-22 02:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ReceiptModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(max_length=250)),
                ('product', models.CharField(max_length=250)),
                ('price', models.FloatField(max_length=100)),
                ('quantity', models.IntegerField()),
                ('hst', models.FloatField(max_length=2)),
                ('date_added', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
