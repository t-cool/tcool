from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index_page'),
    path('count_words', views.count_words, name='count_words_page'),
    path('count_words/<int:id>', views.count_words, name='count_words_page_history'),
    path('word_count_history', views.show_history, name='word_count_history_page'),
]
