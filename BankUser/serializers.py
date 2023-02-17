from rest_framework import serializers
from .models import BankUser
from Bank.models import BankAccount
from Bank.services import create_card


# class BankUserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = BankUser
#         fields = ('first_name', 'last_name', 'email', 'password')
#
#     def create(self, validated_data):
#         instance = super(BankUserSerializer, self).create(validated_data)
#         print(instance)
#         BankAccount.objects.create(user=instance,
#                                    account_number=create_card())
#         return instance
