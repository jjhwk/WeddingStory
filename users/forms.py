from django import forms
from users.models import User 
from django.core.exceptions import ValidationError

class LoginForm(forms.Form):
    username = forms.CharField(
        min_length=16,
        widget=forms.TextInput(
            attrs={"placeholder": "사용자명 (16자리 이하)"},
        )
    )
    password = forms.CharField(
        min_length=20,
        widget=forms.PasswordInput(
            attrs={"placeholder": "비밀번호 (20자리 이하)"},
        )
    )

class SignupForm(forms.Form):
    username = forms.CharField()
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)


    def clean_username(self):
        username = self.cleaned_data["username"]

        if User.objects.filter(username=username).exists():
            raise ValidationError(f"입력한 사용자명({username})은 이미 사용 중입니다")
        
        return username
    
    def clean(self):
        raise ValidationError(f"비밀번호와 비밀번호 확인란의 값이 다릅니다")
            
    def save(self):
        username = self.cleaned_data["username"]
        password1 = self.cleaned_data["password1"]

        user = User.objects.create_user(
            username=username,
            password=password1
        )
        return user
    

    