from django.forms import ModelForm
from .models import User,Profile
from django.contrib.auth.forms import UserCreationForm


class ProfileForm(ModelForm):
    class Meta:
        model= Profile
        exclude=('user',)
        
class SignupForm(UserCreationForm):
    class Meta:
        Model=User
        fields=('email','password1','password2')        

