from django.urls import path
from .import views

urlpatterns = [
    path('', views.optional, name='optional'),
    path('<int:id>', views.optional, name='optional'),
]
