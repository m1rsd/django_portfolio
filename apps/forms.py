from django.forms import ModelForm

from apps.models import ContactEmails


class ContactForm(ModelForm):
    class Meta:
        model = ContactEmails
        fields = ('author', 'email', 'subject', 'message')
