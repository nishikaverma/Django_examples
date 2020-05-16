from django import forms

class Contactforms(forms.Form):
    subject=forms.CharField()
    email=forms.EmailField(required=False)
    msg=forms.CharField()

# for msg='''widget=forms.Textarea'''
# for email='''lable="your email"'''