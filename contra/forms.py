from django import forms
from .models import Contractor

class Contractor_Form(forms.Form):

    class Meta:
        model = Contractor
        field = ('__all__')
