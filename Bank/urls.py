from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'account', BankAccountViewSet)
router.register(r'action', ActionAddMoneyViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('customer/', CustomerList.as_view()),
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls'))
]
