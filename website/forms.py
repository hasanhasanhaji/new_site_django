from website.models import Contact, Newsletter
from django.forms import ModelForm, CharField


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'  # چه فیلدهایی داشته باشه فرم من

    # Override the clean_subject method to make it optional
    # Modify the subject field to be optional

    subject = CharField(required=False, empty_value=None)




class NewsletterForm(ModelForm):
    class Meta:
        model = Newsletter
        fields = '__all__'
