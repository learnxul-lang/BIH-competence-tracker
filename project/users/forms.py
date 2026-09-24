from django import forms
from django.core.exceptions import ValidationError

class User_Registration_Form(forms.Form):
    STUDY_CHOICES = [
        ('DS', 'Data Science'), 
        ('NET', 'Networking'), 
        ('FRT_DEV', 'Front-End Devoloper'), 
        ('BCK_DEV', 'Back_End Developer'),
        ('FS_DEV', 'Full Stack Developer'),
        ]

    LEVELS = [
        ('BGR', 'Beginner'),
        ('JNR', 'Junior'),
    ]

    full_name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Enter your username'})
        )

    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder': 'Enter your email'})
        )

    cellphone = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Enter your cellphone number'})
        )

    study_path = forms.ChoiceField(
        choices=STUDY_CHOICES,
        widget=forms.Select(attrs={'placeholder': 'Select your study path'})
    )

    level = forms.ChoiceField(
        choices=LEVELS,
        widget=forms.Select(attrs={'placeholder': 'Select your level'})
        )

    github_url = forms.URLField(
        widget=forms.URLInput(attrs={'placeholder': 'Paste your Github link'})
        )

    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Enter your password'})
    )

    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Confirm your password'})
    )

    def clean(self):
        cleaned_data = super().clean()

        cleaned_password1 = cleaned_data['password1']
        cleaned_password2 = cleaned_data['password2']

        if cleaned_password1 != cleaned_password2 :
            raise ValidationError('Passwords do not match!')
        return cleaned_data

class Login_Form(forms.Form):

    email = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Enter your email'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs= {'placeholder': 'Enter your password'})
    )
