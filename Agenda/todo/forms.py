from django.forms import ModelForm, DateInput
from  .models import Todo

class TodoForm(ModelForm):
    class Meta:
        model = Todo
        exclude = ('date',)
        widgets = {
            'fecha_fin': DateInput(attrs={'type':'date'}),
        }