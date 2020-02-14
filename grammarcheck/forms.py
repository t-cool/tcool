from django import forms


class GrammarCheckForm(forms.Form):
    text_input = forms.CharField(label="Enter some text",
                                 widget=forms.Textarea(attrs={'class': 'form-control'}))
