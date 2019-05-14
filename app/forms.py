from django import forms
from django.forms import ModelChoiceField
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from app.models import Account, Category, Publication, Group, Comment
import datetime

DEPARTMENT_CHOICES= (
        ('IG', 'IG'),
        ('GBA', 'GBA'),
        ('EGC', 'EGC'),
        ('MAT', 'MAT'),
        ('MEA', 'MEA'),
        ('MI', 'MI'),
        ('MSI', 'MSI'),
        ('SE', 'SE'),
        ('STE', 'STE'),
    )

YEAR_IN_SCHOOL_CHOICES = (
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
    )

#forms for connexion
class SignInForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(label='password', widget=forms.PasswordInput) #widget permit to hide the password

#---------CREATING FORMS-------

#forms for create an account
class SignUpFormAccount(UserCreationForm):
    birthDate = forms.DateField(label="birth date",widget = forms.SelectDateWidget(years=range(1900,2100)))
    department = forms.ChoiceField(widget=forms.Select, choices=DEPARTMENT_CHOICES)
    year_in_school = forms.ChoiceField(widget=forms.Select, choices=YEAR_IN_SCHOOL_CHOICES)
    githubLink = forms.URLField(label="github link", required=False)
    linkedInLink = forms.URLField(label="linkedIn link", required=False)
    class Meta:
        model = User
        fields = ('username','first_name','last_name','birthDate','email','department','year_in_school','githubLink','linkedInLink','password1','password2',)

#forms to create group
class GroupForm(forms.ModelForm):
    nameGroup = forms.CharField(label="group name")
    class Meta:
        model = Group
        fields = ('nameGroup',)


#----------UPDATING FORMS-------

class UpdateAccountForm(forms.Form):
    first_name = forms.CharField(label = "Prénom")
    last_name = forms.CharField(label = "Nom")
    email = forms.EmailField(label = "Adresse éléctonique")
    birthDate = forms.DateField(label="birth date",widget = forms.SelectDateWidget(years=range(1900,2100)))
    department = forms.ChoiceField(widget=forms.Select, choices=DEPARTMENT_CHOICES)
    year_in_school = forms.ChoiceField(widget=forms.Select, choices=YEAR_IN_SCHOOL_CHOICES)
    githubLink = forms.URLField(label="github link", required=False)
    linkedInLink = forms.URLField(label="linkedIn link", required=False)
