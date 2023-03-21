from django.urls import path
from quiz import views
app_name='quiz'
urlpatterns=[
    path('', views.QuizListView.as_view(), name='quiz_list')
]