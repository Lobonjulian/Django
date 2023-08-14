from django.urls import path
from . import views

urlpatterns = [
    path('queries/', views.queries,),
]
