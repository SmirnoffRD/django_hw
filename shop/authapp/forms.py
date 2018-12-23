from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import Custom_User


class CustomUser_LoginForm(AuthenticationForm):
    class Meta:
        model = Custom_User
        fields = ('username', 'password')
    
    def __init__(self, *args, **kwargs):
        super(CustomUser_LoginForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            print(field.help_text)

class CustomUser_RegistrationForm(UserCreationForm):
    class Meta:
        model = Custom_User
        fields = ('username', 'first_name', 'last_name', 'password1', 'password2', 'age', 'email', 'avatar')
        
    def __init__(self, *args, **kwargs):
        super(CustomUser_RegistrationForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''

    # def clean_age(self):
    #     data = self.cleaned_data['password1']
    #     if len(data) < 10:
    #         raise forms.ValidationError("Слишком короткий пароль")

    #     return data