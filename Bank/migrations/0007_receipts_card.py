# Generated by Django 4.1.7 on 2023-02-20 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Bank', '0006_receipts'),
    ]

    operations = [
        migrations.AddField(
            model_name='receipts',
            name='card',
            field=models.CharField(blank=True, max_length=650, verbose_name='Card'),
        ),
    ]