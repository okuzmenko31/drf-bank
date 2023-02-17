# Generated by Django 4.1.7 on 2023-02-17 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BankUser', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bankuser',
            options={'verbose_name': 'user', 'verbose_name_plural': 'users'},
        ),
        migrations.AlterField(
            model_name='bankuser',
            name='email',
            field=models.EmailField(blank=True, max_length=254, verbose_name='email address'),
        ),
    ]