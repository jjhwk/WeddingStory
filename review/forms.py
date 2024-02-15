from django import forms
from review.models import Post



class PostForm(forms.ModelForm): 
    class Meta:   
        model = Post
        fields = [
            "content",
        ]