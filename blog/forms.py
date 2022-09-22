from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from .models import Gun, Comments


class CreateUser(forms.ModelForm):
    username = forms.CharField(label = False, widget=forms.TextInput(attrs={'placeholder': 'Nazwa użytkownika'}))
    password = forms.CharField(label = False, widget=forms.PasswordInput(attrs={'placeholder': 'Hasło'}))
    password2 = forms.CharField(label = False, widget=forms.PasswordInput(attrs={'placeholder': 'Powtórz hasło'}))
    
    class Meta:
        model = User
        fields = ('username',)
        help_texts = {
            'username': None,
        }

    
    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Hasła nie są identyczne')
        return cd['password2']

class Login(AuthenticationForm):
    username = forms.CharField(label=False, widget=forms.TextInput(attrs={'placeholder': 'Nazwa użytkownika'}))
    password = forms.CharField(label=False, widget=forms.PasswordInput(attrs={'placeholder':'Hasło'}))


class CreateNewGun(forms.ModelForm):
    gun_name = forms.CharField(label = False, widget=forms.TextInput(attrs={'placeholder': 'Nazwa broni'}))
    gun_num = forms.CharField(label = False, widget=forms.TextInput(attrs={'placeholder': 'Numer seryjny'}))
    gun_body = forms.CharField(label = False, widget=forms.Textarea(attrs={'placeholder': 'Opis...', 'cols': 35, 'rows': 20}))
    gun_pic = forms.ImageField(label = False,  widget=forms.FileInput(attrs={'id': 'image_input'}))

    class Meta:
        model = Gun
        fields = ('gun_name', 'gun_num','gun_body', 'caliber', 'gun_pic')
        
        labels = {
            'caliber': 'Nabój'
        }
    
    
class Update(forms.ModelForm):
    
    class Meta:
        model = Comments
        fields = ('comment', )
        labels = {
            'comment': False
            }
        widgets = {
            'comment': forms.Textarea(attrs= {'placeholder': 'Komentarz...'})

        }