from rest_framework import serializers
from .models import BankAccount, Customer, ActionAddMoney, Transfer, Transaction, Receipts


class BankAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankAccount
        fields = ('id', 'account_number', 'balance')
        read_only_fields = ('id', 'account_number', 'balance')


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('id', 'first_name', 'last_name', 'country', 'city', 'image')

    def create(self, validated_data):
        # override standard method to create customer without pk in url
        validated_data['user_id'] = self.context['request'].user.id
        return super(CustomerSerializer, self).create(validated_data)


class ActionAddMoneySerializer(serializers.ModelSerializer):
    class Meta:
        model = ActionAddMoney
        fields = ('id', 'bank_account', 'amount')

    def create(self, validated_data):
        if validated_data['bank_account'].balance + validated_data['amount'] > 0:
            validated_data['bank_account'].balance += validated_data['amount']
            validated_data['bank_account'].save()
        else:
            raise serializers.ValidationError('Invalid amount')

        return super(ActionAddMoneySerializer, self).create(validated_data)


class TransferSerializer(serializers.ModelSerializer):

    def __init__(self, *args, **kwargs):
        super(TransferSerializer, self).__init__(*args, **kwargs)
        if 'request' in self.context:
            self.fields['from_account'].queryset = self.fields['from_account'] \
                .queryset.filter(user=self.context['view'].request.user)

    class Meta:
        model = Transfer
        fields = ('id', 'category', 'from_account', 'to_account', 'amount', 'description')
        read_only_fields = ('id',)

    def create(self, validated_data):
        if validated_data['from_account'].balance > 0:
            try:
                to_acc = BankAccount.objects.get(account_number=validated_data['to_account'])
                if to_acc.balance + validated_data['amount'] > 0:
                    to_acc.balance += validated_data['amount']
                    to_acc.save()
                else:
                    raise serializers.ValidationError('Invalid amount')
            except Exception as a:
                print(a)
                raise serializers.ValidationError('No such account with this card number')
            return super(TransferSerializer, self).create(validated_data)
        else:
            raise serializers.ValidationError('Not enough money')


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ('id', 'category', 'transfer', 'amount')
        read_only_fields = ('id', 'transfer', 'amount')


class ReceiptsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Receipts
        fields = ('id', 'transfer', 'user', 'amount', 'description')
