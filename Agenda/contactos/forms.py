from django.forms import ModelForm
from  .models import Contacto

class ContactosForm(ModelForm):
    class Meta:
        model = Contacto
        fields = '__all__'