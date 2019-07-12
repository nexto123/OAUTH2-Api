import re
import time
from django.conf import settings
from django import forms
from django.forms import ValidationError
from allauth.account.adapter import DefaultAccountAdapter
from django.contrib.auth.password_validation import validate_password
from allauth.account.adapter import app_settings



class MyAccountAdapter(DefaultAccountAdapter):

    def clean_password(self, password, user=None):
        min_length = app_settings.PASSWORD_MIN_LENGTH

        if re.match(r'^(?=.*?\d)(?=.*?[A-Z])(?=.*?[a-z])[A-Za-z\d]{8,}$', password):
            return password
        else:
            raise forms.ValidationError(("Password must be a minimum of 6 "
                                          "characters. & must start with Capital a letter..").format(min_length))


