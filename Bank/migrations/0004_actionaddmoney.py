# Generated by Django 4.1.7 on 2023-02-17 23:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Bank', '0003_customer_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActionAddMoney',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=15, verbose_name='Amount')),
                ('bank_account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Bank.bankaccount', verbose_name='Bank account')),
            ],
            options={
                'verbose_name': 'add money action',
                'verbose_name_plural': 'Add money actions',
            },
        ),
    ]
