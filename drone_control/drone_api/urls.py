from django.urls import path
from .views import DroneControlView

urlpatterns = [
    path('control/', DroneControlView.as_view(), name='drone-control'),
]