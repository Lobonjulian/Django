from django import forms

class CommentForm(forms.Form):
    name = forms.CharField(label='Escribe tu nombre', max_length=100)
    url = forms.URLField(label='tu sitio web', required=False, initial='http://')
    comment = forms.CharField()
    
class ConctactForm(forms.Form):
    name = forms.CharField(label='Nombre:', 
                            max_length=50,
                            widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='email:', 
                                max_length=50,
                                widget= forms.EmailInput(attrs={'class': 'form-control'}))
    message = forms.CharField(label='Mensaje:',
                                widget= forms.Textarea(attrs={'class': 'form-control'}))