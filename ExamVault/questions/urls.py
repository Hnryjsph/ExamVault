from django.urls import path
from . import views

app_name = 'questions'

urlpatterns = [
    path('', views.questions, name='questions'),
    path('content/<int:id>/', views.details, name='details'),
    path('collections/', views.collections, name='collections'),

   
]
