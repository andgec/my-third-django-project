'''
Created on Jun 21, 2017

@author: andrius
'''

from django import forms

from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)