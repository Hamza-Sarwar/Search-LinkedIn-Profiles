from django import forms


class TempForm(forms.Form):
    country = forms.CharField()
    state = forms.CharField()
    name = forms.CharField()
    phone = forms.CharField()
    email = forms.CharField()
