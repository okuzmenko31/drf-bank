from django.db import models
from django.conf import settings


class Customer(models.Model):
    first_name = models.CharField(max_length=255, verbose_name='First name')
    last_name = models.CharField(max_length=255, verbose_name='Last name')
    country = models.CharField(max_length=200, verbose_name='Country')
    city = models.CharField(max_length=200, verbose_name='City')
    image = models.ImageField(upload_to='bank/customer_images/',
                              blank=True,
                              verbose_name='Customer image')
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE,
                             verbose_name='User')

    class Meta:
        verbose_name = 'customer'
        verbose_name_plural = 'Customers'

    def __str__(self):
        return f'{self.user} {self.first_name} {self.last_name}'


class TransferCategory(models.Model):
    name = models.CharField(max_length=355, verbose_name='Category name')

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'Categories of transfers'

    def __str__(self):
        return f'Category: {self.name}'


class BankAccount(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE,
                             verbose_name='Owner')
    account_number = models.CharField(max_length=650, verbose_name='Customer account number')
    balance = models.DecimalField(max_digits=15,
                                  decimal_places=2,
                                  verbose_name='Bank account balance',
                                  default=0)


class Meta:
    verbose_name = 'account'
    verbose_name_plural = 'Bank accounts'


def __str__(self):
    return f'{self.user}, account_number: {self.account_number}, balance: {self.balance}'


class Transfer(models.Model):
    category = models.ForeignKey(TransferCategory,
                                 on_delete=models.CASCADE,
                                 verbose_name='Transfer category(Optional)',
                                 null=True,
                                 blank=True)
    from_account = models.ForeignKey(BankAccount,
                                     on_delete=models.CASCADE,
                                     verbose_name='From account')
    to_account = models.CharField(max_length=650, verbose_name='Recipient\'s bank account')
    amount = models.DecimalField(max_digits=15,
                                 decimal_places=2,
                                 default=0,
                                 verbose_name='Amount of transaction')
    description = models.CharField(max_length=5000,
                                   verbose_name='Description of transfer',
                                   blank=True)

    class Meta:
        verbose_name = 'transfer'
        verbose_name_plural = 'Transfers'

    def __str__(self):
        return f'Transfer ID: {self.id}'


class Transaction(models.Model):
    category = models.ForeignKey(TransferCategory,
                                 on_delete=models.CASCADE,
                                 verbose_name='Category of transfer',
                                 null=True,
                                 blank=True)
    transfer = models.ForeignKey(Transfer,
                                 on_delete=models.CASCADE,
                                 verbose_name='Transfer')
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE,
                             verbose_name='Customer')
    amount = models.DecimalField(max_digits=15,
                                 decimal_places=2,
                                 verbose_name='Amount of transaction',
                                 default=0)

    class Meta:
        verbose_name = 'transaction'
        verbose_name_plural = 'Transactions'

    def __str__(self):
        return f'Transaction ID: {self.id}, sender: {self.user}, category: {self.category}'


class ActionAddMoney(models.Model):
    bank_account = models.ForeignKey(BankAccount,
                                     on_delete=models.CASCADE,
                                     verbose_name='Bank account')
    amount = models.DecimalField(max_digits=15,
                                 decimal_places=2,
                                 verbose_name='Amount')

    class Meta:
        verbose_name = 'add money action'
        verbose_name_plural = 'Add money actions'

    def __str__(self):
        return f'{self.bank_account.account_number}, amount: {self.amount}'


class Receipts(models.Model):
    card = models.CharField(max_length=650,
                            verbose_name='Card',
                            blank=True)
    transfer = models.ForeignKey(Transfer,
                                 on_delete=models.CASCADE,
                                 verbose_name='Transfer')
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE,
                             verbose_name='Customer')
    amount = models.DecimalField(max_digits=15,
                                 decimal_places=2,
                                 verbose_name='Amount of transaction',
                                 default=0)
    sender = models.ForeignKey(BankAccount,
                               on_delete=models.CASCADE,
                               verbose_name='Sender')
    description = models.CharField(max_length=5000,
                                   verbose_name='Description of transfer',
                                   blank=True)

    class Meta:
        verbose_name = 'receipt'
        verbose_name_plural = 'Receipts'

    def __str__(self):
        return f'Receipt ID: {self.id}, sender: {self.user}, amount: {self.amount}'
