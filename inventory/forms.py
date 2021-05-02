from django import forms 
from .models import *

class mobileform(forms.ModelForm):
    class Meta:
            model = mobile
            fields = ('idno','brand','name','ram','storage','price','stock')




