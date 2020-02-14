from django import forms


class GrammarCheckForm(forms.Form):
    email_address = forms.EmailField(label="Email address",
                                     widget=forms.TextInput(attrs={'class': 'form-control'}))
