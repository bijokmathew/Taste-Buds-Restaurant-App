from . import views
from django.urls import path

urlpatterns = [
    path('', views.base.as_view(), name='base')
]


