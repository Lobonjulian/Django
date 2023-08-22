from django import forms

class CommentForm(forms.Form):
    name = forms.CharField(label='Escribe tu nombre', max_length=100)
    url = forms.URLField(label='tu sitio web', required=False, initial='http://')
    comment = forms.CharField()