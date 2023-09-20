from django.urls import path
from .import views

from injection.views import (injection1,
)

app_name = 'core'

urlpatterns = [
    path('', views. index, name='index'),

    path('injection1/', injection1, name='injection1'),
]