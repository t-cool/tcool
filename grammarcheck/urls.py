from django.urls import path, re_path

from . import views

urlpatterns = [
    path('check_grammar', views.check_grammar, name='check_grammar_page'),
    path('check_grammar/<int:id>', views.check_grammar, name='check_grammar_page_history'),
    path('grammar_check_history', views.show_history, name='grammar_check_history_page'),
]
