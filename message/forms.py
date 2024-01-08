from django import forms
from ckeditor.widgets import CKEditorWidget
from .models import Message

class EmailForm(forms.ModelForm):

    class Meta:
        model = Message
        fields = ['recipients','subject', 'body_html']
        widgets = {
            'subject':forms.TextInput(attrs={'class':'form-control w-100'}),
            'body_html':CKEditorWidget(attrs={'class':'form-control w-100'}),          
        }