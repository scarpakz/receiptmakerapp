# Generated by Django 5.1.4 on 2024-12-28 01:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_receiptmodel_notes_receiptmodel_purchaser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receiptmodel',
            name='hst',
            field=models.FloatField(default=15, max_length=2),
        ),
    ]