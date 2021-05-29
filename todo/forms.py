from django import forms

from todo.models import CustomUser


class UserForm(forms.ModelForm):
    password2 = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
