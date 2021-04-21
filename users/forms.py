from allauth.account.forms import SignupForm
from django import forms
from django.forms.widgets import DateInput
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class CustomSignupForm(SignupForm):
    # BIRTHYEARS = [timezone.now().year - b for b in range(100)]
    name = forms.CharField(
        max_length=50,
        strip=True,
        required=True,
        widget=forms.TextInput(attrs={"placeholder": _("What's your name?"), "autocomplete": "name"}),
    )
    # birthday = forms.DateField(widget=forms.SelectDateWidget(years=BIRTHYEARS))

    # def save(self, request):
    #     user = super(CustomSignupForm, self).save(request)
    #     return user
