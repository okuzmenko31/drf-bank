from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import viewsets
from rest_framework import mixins
from .models import BankAccount, Customer, Transfer
from rest_framework.generics import ListCreateAPIView, ListAPIView
from .serializers import CustomerSerializer, BankAccountSerializer, \
    ActionAddMoneySerializer, TransferSerializer, TransactionSerializer
from .services import create_card
from .models import ActionAddMoney, Transaction


class CustomerList(ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class BankAccountViewSet(viewsets.GenericViewSet,
                         mixins.ListModelMixin,
                         mixins.CreateModelMixin):
    queryset = BankAccount.objects.all()
    serializer_class = BankAccountSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user, account_number=create_card())


class ActionAddMoneyViewSet(viewsets.GenericViewSet,
                            mixins.ListModelMixin,
                            mixins.CreateModelMixin):
    queryset = ActionAddMoney.objects.all()
    serializer_class = ActionAddMoneySerializer
    permission_classes = (IsAdminUser,)
    authentication_classes = (TokenAuthentication,)


class TransferViewSet(viewsets.GenericViewSet,
                      mixins.CreateModelMixin):
    queryset = Transfer.objects.all()
    serializer_class = TransferSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

    def get_queryset(self):
        return self.queryset.filter(self.request.data['from-account'])

    def perform_create(self, serializer):
        from_acc_pk = self.request.data['from_account']
        from_acc = BankAccount.objects.get(pk=from_acc_pk)
        transfer = serializer.save(from_account=from_acc)
        from_acc.balance -= transfer.amount
        from_acc.save()

        if transfer.category:
            Transaction.objects.create(category=transfer.category,
                                       transfer=transfer,
                                       user=self.request.user,
                                       amount=transfer.amount)
        else:
            Transaction.objects.create(transfer=transfer,
                                       user=self.request.user,
                                       amount=transfer.amount)


class TransactionAPIView(ListAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)
