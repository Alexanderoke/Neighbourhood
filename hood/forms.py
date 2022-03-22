from django import forms
from .models import Bussiness

class BussinessRegisterForm(forms.ModelForm):
  Neighbourhood = forms.Charfield()

  class Meta:
    model=Bussiness
    fields=['owner_name','Business_name', 'Business_email','password2']