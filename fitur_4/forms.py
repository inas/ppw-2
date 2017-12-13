from django import forms

class Message_Form(forms.Form):
    error_messages = {
        'required': 'You haven\'t written anything',
    }

    description_attrs = {
        'type': 'text',
        'cols': 70,
        'rows': 4,
        'class': 'todo-status-textarea',
        'placeholder':'masukkan tanggapan'
    }

    description = forms.CharField(label='', required=True, widget=forms.Textarea(attrs=description_attrs))