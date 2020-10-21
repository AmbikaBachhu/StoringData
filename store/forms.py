from django import forms

from .models import Storing


class StoringForm(forms.ModelForm):
    class Meta:
        model = Storing
        fields = "__all__"
