from django.urls import path
from .views import *

urlpatterns = [
    path('buttons/', buttons, name="buttons"),  # playground/buttons
    path('text/', text, name="text"),  # playground/buttons
    path('youtube/', youtube, name="youtube"),  # playground/youtube
]