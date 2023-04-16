from os import access
from django.dispatch import receiver
from django.db.models.signals import pre_save, post_save
from django.contrib.auth.signals import (
    user_logged_in,
    user_logged_out,
    user_login_failed,
)

# from .models import
from django.contrib.sessions.models import Session
import pyotp
import requests
from django.conf import settings

@receiver(user_logged_in)
def perform_login_to_savings(request, user, **kwargs):
    try:
        perform_access_auth(user)
    except:
        pass