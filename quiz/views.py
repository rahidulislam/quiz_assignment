from django.shortcuts import render
from django.views import generic

from quiz.models import Quiz


# Create your views here.

class QuizListView(generic.ListView):
    model = Quiz
    template_name = "quiz/quiz_list.html"
    context_object_name = "quizes"
