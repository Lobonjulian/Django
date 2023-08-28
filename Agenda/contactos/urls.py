from django.urls import path
from . import views 

urlpatterns = [
    path('', views.index, name='contactos'),
    path('<letter>', views.index, name='contactos'),
    path('view/<int:id>', views.view, name='contacto_view'),
    path('edit/<int:id>', views.edit, name='contacto_edit'),
    path('create/', views.create, name='contacto_create'),
    path('delete/<int:id>', views.delete, name='contacto_delete'),
]
