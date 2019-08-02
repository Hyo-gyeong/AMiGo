from django import forms
from .models import Korean, Lforeigner, Sforeigner, K_Comment, Lf_Comment, Sf_Comment

class KNew(forms.ModelForm): 
    class Meta: 
        model = Korean 
        fields = ['image', 'title', 'sex', 'nation', 'region', 'interest', 'body'] 

class LfNew(forms.ModelForm): 
    class Meta: 
        model = Lforeigner 
        fields = ['image', 'title', 'sex', 'nation', 'region', 'interest', 'body'] 

class SfNew(forms.ModelForm): 
    class Meta: 
        model = Sforeigner 
        fields = ['image', 'title', 'sex', 'nation', 'region', 'interest', 'body'] 

class K_CommentForm(forms.ModelForm):
    class Meta:
        model = K_Comment
        fields = ['kcontents']

class Lf_CommentForm(forms.ModelForm):
    class Meta:
        model = Lf_Comment
        fields = ['lfcontents']

class Sf_CommentForm(forms.ModelForm):
    class Meta:
        model = Sf_Comment
        fields = ['sfcontents']

