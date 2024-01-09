from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from chinese.models import BlogPost, ContactMessage


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'message', "phone_no",]


class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'content', ]
