from django import forms


class WordCountForm(forms.Form):
    text_input = forms.CharField(label="Enter some text",
                                 widget=forms.Textarea(attrs={'class': 'form-control'}))
