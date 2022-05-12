
from django import forms
from .models import DemoUser

ROLE_CHOICES = [
 ('Doctor', 'Doctor'),
 ('Patient', 'Patient')
]


class DemoUserForm(forms.ModelForm):
    role = forms.ChoiceField(choices=ROLE_CHOICES, widget=forms.RadioSelect)
    class Meta:
        model= DemoUser
        fields = ['fname','lname','username','email','role',
        'pass1','pass2','city','state','pin','profile_img']
        labels = {'fname':'First Name','lname':'Last Name','username':'Username',
        'email':'Email id','role':'Role','pass1':'password','pass2':'Confirm Password','city':'City',
        'state':'State','pin':'PinCode','profile_img':'Image'}

        widgets = {
        'fname':forms.TextInput(attrs={'class':'form-control'}),
        'lname':forms.TextInput(attrs={'class':'form-control'}),
        'username':forms.TextInput(attrs={'class':'form-control'}),
        'email':forms.EmailInput(attrs={'class':'form-control'}),
        'pass1':forms.PasswordInput(attrs={'class':'form-control'}),
        'pass2':forms.PasswordInput(attrs={'class':'form-control'}),
        'city':forms.TextInput(attrs={'class':'form-control'}),
        'state':forms.TextInput(attrs={'class':'form-control'}),
        'pin':forms.NumberInput(attrs={'class':'form-control'}),
  }
    