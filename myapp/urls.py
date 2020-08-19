from . import views
from django.urls import path

app_name = 'myapp'

urlpatterns = [
    path('activity/', views.Activity.as_view(),
         name='Activity')
    ]