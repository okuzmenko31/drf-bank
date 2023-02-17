from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import viewsets
from rest_framework import mixins
from .models import BankAccount, Customer
from rest_framework.generics import ListCreateAPIView
from .serializers import CustomerSerializer, BankAccountSerializer, ActionAddMoneySerializer
from .services import create_card
from .models import ActionAddMoney


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
