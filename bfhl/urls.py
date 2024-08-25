from django.urls import path
from .views import BFHLAPIView

urlpatterns = [
    path('', BFHLAPIView.as_view(), name='bfhl'),
]
