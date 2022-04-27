from django import forms
from django.forms import ModelForm, HiddenInput
from django.utils.dateparse import parse_datetime
from .models import Deployment, Equipment
# Form to Add Site Equipment
#Remove site Equipment

#Change instrument - Add or Remove
class Add_Instrument(forms.Form):
    date = forms.DateField(required=True)
    time = forms.TimeField(required=True)
    site_eq = forms.CharField(max_length=24,widget = forms.HiddenInput())
    instrument = forms.ModelChoiceField(Equipment.objects.all())
    def get_datetime(self):
        return(parse_datetime(f"{self.cleaned_data['date']} {self.cleaned_data['time']}"))

class Remove_Instrument(forms.Form):
    deployment = forms.CharField(max_length=24)
    date = forms.DateField()
    time = forms.TimeField()

    def get_datetime(self):
        return(parse_datetime(f"{self.cleaned_data['date']} {self.cleaned_data['time']}"))

