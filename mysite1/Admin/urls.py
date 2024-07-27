from django.urls import path
from .views import *


urlpatterns = [
    path('', Admin1),
    path('Main_Admin', Main_Admin),
    path('Chart', Revenue),
]