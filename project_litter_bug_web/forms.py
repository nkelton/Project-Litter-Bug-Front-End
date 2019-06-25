from captcha.fields import ReCaptchaField
from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=254)
    message = forms.CharField(
        max_length=2000,
        widget=forms.Textarea()
    )
    captcha = ReCaptchaField()

    def clean(self):
        cleaned_data = super(ContactForm, self).clean()
        name = cleaned_data.get('name')
        email = cleaned_data.get('email')
        message = cleaned_data.get('message')
        if not name:
            raise forms.ValidationError('Please enter a valid name')
        if not email:
            raise forms.ValidationError('Please enter a valid email')
        if not message:
            raise forms.ValidationError('Please enter a valid message')
