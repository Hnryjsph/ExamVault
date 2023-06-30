from django.urls import path
from . import views

app_name = 'questions'

urlpatterns = [
    path('', views.questions, name='questions'),
    path('content/<int:id>/', views.details, name='details'),
    path('collections/', views.collections, name='collections'),
    path('search/', views.search, name='search'),
    path('bookmark/<int:id>/', views.bookmark, name='bookmark'),
    path('collection_remove/<int:id>/', views.collection_remove, name='collection_remove'),
    path('question_remove/<int:id>/', views.question_remove, name='question_remove'),
   
]
