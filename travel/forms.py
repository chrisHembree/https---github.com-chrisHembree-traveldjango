from django import forms
from .models import DestinationDetails


class CreateDestinationDetailsForm(forms.ModelForm):
    class Meta:
        model = DestinationDetails
        fields = ['destination', 'accommodations']





