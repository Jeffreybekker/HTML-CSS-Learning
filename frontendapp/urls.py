from django.urls import path
from .views import *

urlpatterns = [
    path('buttons/', buttons, name="buttons")  # playground/buttons
]