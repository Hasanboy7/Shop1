from django import forms
from .models import Comment,Kitob,Tillar

class CommentForm(forms.ModelForm):
    start_give=forms.IntegerField(max_value=5,min_value=1)
    comment_text=forms.CharField(widget=forms.Textarea(attrs={'rows':5}))
    class Meta:
        model=Comment
        fields=('comment_text','start_give')

class AddKitob(forms.ModelForm):

    class Meta:
        model=Kitob
        fields=('name','til','body','img')

class AddTilForm(forms.ModelForm):

    class Meta:
        model=Tillar
        fields='__all__'