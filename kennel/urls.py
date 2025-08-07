from django.urls import path
from kennel import views

app_name = 'kennel'

urlpatterns = [
    path('', views.index, name='index'),
]
