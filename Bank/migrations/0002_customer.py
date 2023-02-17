# Generated by Django 4.1.7 on 2023-02-17 22:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Bank', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255, verbose_name='First name')),
                ('last_name', models.CharField(max_length=255, verbose_name='Last name')),
                ('country', models.CharField(max_length=200, verbose_name='Country')),
                ('city', models.CharField(max_length=200, verbose_name='City')),
                ('image', models.ImageField(blank=True, upload_to='bank/customer_images/', verbose_name='Customer image')),
            ],
            options={
                'verbose_name': 'customer',
                'verbose_name_plural': 'Customers',
            },
        ),
    ]
