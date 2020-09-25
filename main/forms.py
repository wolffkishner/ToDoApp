from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *

# code


class createUserForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name',
                  'username', 'password1', 'password2']


class createTaskForm(ModelForm):
    class Meta:
        model = TaskInfo
        fields = '__all__'
