from django import forms


class QForm(forms.Form):
    query = forms.CharField()