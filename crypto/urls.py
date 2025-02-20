from django.urls import path
from .views import home, encrypt_view, decrypt_view

urlpatterns = [
    path('', home, name='home'),
    path('encrypt/', encrypt_view, name='encrypt'),
    path('decrypt/', decrypt_view, name='decrypt'),
]