from django.forms import ModelForm
from django import forms
from .models import Organization, Program


class OrganizationForm(ModelForm):
    class Meta:
        model = Organization
        fields = "__all__"

class ProgramForm(forms.ModelForm):
    class Meta:
        model = Program
        fields = ['prog_name', 'college']
