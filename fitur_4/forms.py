from django import forms

class Message_Form(forms.Form):
    attrs = {
        'class': 'form-control'
    }
    message = forms.CharField(widget=forms.Textarea(attrs=attrs), required=True)