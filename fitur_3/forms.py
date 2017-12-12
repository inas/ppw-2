from django import forms

class Message_Form(forms.Form):
    error_messages = {
        'required': 'Tolong isi input ini',
        'invalid': 'Isi input dengan email',
    }
    attrs = {
        'class': 'form-control'
    }

    title_attrs = {
        'class': 'form-control',
        'placeholder':'This post is about...'
    }

    message_attrs = {
        'class': 'form-control',
        'placeholder':'Your post is...'
    }

    title = forms.CharField(label='Judul Forum', required=True, max_length=30, widget=forms.TextInput(attrs=title_attrs))
    message = forms.CharField(widget=forms.Textarea(attrs=message_attrs), required=True)