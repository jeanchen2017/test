from django import forms

from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('post_subject', 'post_content', 'avatar_id', )

class AnswerForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('post_content', 'avatar_id',)
