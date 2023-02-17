from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated

from .serializers import BankUserSerializer


# class BankUserDetail(CreateAPIView):
#     serializer_class = BankUserSerializer
#     authentication_classes = (TokenAuthentication,)
