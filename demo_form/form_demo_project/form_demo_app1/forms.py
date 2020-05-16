from django import forms

class Contactforms(forms.Form):
    
    email=forms.EmailField(required=False)
    password=forms.CharField()