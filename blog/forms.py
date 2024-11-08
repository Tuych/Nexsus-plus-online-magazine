from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']

        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': '8', 'cols': '45', 'placeholder': 'Write your comment'})
        }

