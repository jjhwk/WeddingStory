from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from .models import User, UserManager
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
    



class UserCreationForm(forms.ModelForm):
    # 사용자 생성 폼
    email = forms.EmailField(
        label='Email',
        required=True,
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': ('Email address'),
                'required': 'True',
            }
        )
    )
    name = forms.CharField(
        label='name',
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': ('Name'),
                'required': 'True',
            }
        )
    )
    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': ('Password'),
                'required': 'True',
            }
        )
    )
    password2 = forms.CharField(
        label='Password confirmation',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': ('Password confirmation'),
                'required': 'True',
            }
        )
    )

    class Meta:
        model = User
        fields = ('email', 'name')

    def clean_password2(self):
        # 두 비밀번호 입력 일치 확인
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserCreationForm, self).save(commit=False)
        user.email = UserManager.normalize_email(self.cleaned_data['email'])
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    # 비밀번호 변경 폼
    password = ReadOnlyPasswordHashField(
        label='Password'
    )

    class Meta:
        model = User
        fields = ('email', 'password', 'is_superuser')

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]




# class UserForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ['ID','name', 'address', 'profile_picture']


# class ProfileForm(forms.ModelForm):
#     profile_photo = forms.ImageField(required=False) # 선택적으로 입력할 수 있음.
    
#     class Meta:
#         model = Profile
#         fields = ['nickname', 'profile_picture']