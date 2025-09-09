from django import forms
from apps.contact.models import ContactModel

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactModel
        exclude = ['is_read', 'comment']


    def clean(self):
        print("1. object level validation")
        print(self.cleaned_data)
        return super().clean()

    def clean_email(self):
        print("2. field level validation")
        your_email: str = self.cleaned_data.get('email')
        if '@' not in your_email:
            raise forms.ValidationError("Email manzilda '@' belgisi bo'lishi kerak")
        return self.cleaned_data.get('email')