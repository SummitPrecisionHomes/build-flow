from django.urls import path
from .views import predict_schedule

urlpatterns = [
    path('predict/', predict_schedule, name='predict'),
]