from django.urls import path
from .views import blog, detail_blog

urlpatterns = [
    path('', blog, name='blog'),
    path('<slug:slug>/', detail_blog, name="detail")
]