from .models import Project,Comment,Like
from django import forms


class NewProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ['editor']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['project' ]
    
class LikeForm(forms.ModelForm):
    class Meta:
        model = Like
        exclude = ['project']
           
       
