from .models import BankAccount, Receipts


class CreateReceipt:

    @staticmethod
    def create_receipt(transfer):
        try:
            to_acc = BankAccount.objects.get(account_number=transfer.to_account)
        except Exception as a:
            print(a)
            raise ValueError('No such account')

        Receipts.objects.create(card=to_acc.account_number,
                                transfer=transfer,
                                user=to_acc.user,
                                amount=transfer.amount,
                                sender=transfer.from_account,
                                description=transfer.description)
