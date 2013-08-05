from django import forms

class PayForm(forms.Form):
	name = forms.CharField(max_length=100, required=True)
	email = forms.EmailField(max_length=75, required=True)
	phone = forms.CharField(max_length=10, required=True)
