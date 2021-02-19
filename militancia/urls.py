from django.urls import path
from .views import militancia

urlpatterns = [
    path('', militancia, name='militancia')
]