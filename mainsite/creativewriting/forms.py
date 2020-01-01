from django import forms
from .models import Articles
from django.contrib.auth.models import User

class ArticlePost(forms.ModelForm):
    
    class Meta:
        model = Articles
        fields = ('title','description','content')

class Register(forms.ModelForm):
    password = forms.CharField(widget = forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username','email','password')

