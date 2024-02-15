from django import forms
from review.models import Post, Comment



class PostForm(forms.ModelForm): 
    class Meta:   
        model = Post
        fields = [
            "title",
            "score",  
            "content",
        ]
        
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            "post",      
            "content",
        ]