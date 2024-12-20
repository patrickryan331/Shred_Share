from django import forms
from .models import Post

class PostCreateForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['title', 'body', 'image']
        widgets = {
            'image': forms.FileInput(attrs={'class': 'form-control'})
        }


class ContactForm(forms.Form):
    name =  forms.CharField(max_length=250)
    email = forms.EmailField()
    subject = forms.CharField(max_length=250)
    message = forms.CharField()

