from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .forms import WordCountForm
from django.contrib.auth.decorators import login_required
from .helpers import count_and_sort_words
from .models import WordCounterHistory


def index(request):
    return render(request, "wordcounter/index.html", {})


@login_required
def count_words(request, id=None):
    if request.method == "POST":
        form = WordCountForm(request.POST)
        word_counts = count_and_sort_words(form.data["text_input"])
        if form.is_valid():
            history = WordCounterHistory()
            history_item = request.GET.get("id", None)
            history.user = request.user
            history.search_text = form.data["text_input"]
            if not request.POST.get("id"):
                history._picked_obj = word_counts
                history.save()
            return render(request, "wordcounter/count_words.html",
                          {'form': form,
                           'sorted_word_counts': word_counts})
    else:
        form = WordCountForm()
        template_context = {"form": form}
        if id:
            history_item = get_object_or_404(WordCounterHistory, id=id)
            if history_item._picked_obj:
                template_context["sorted_word_counts"] = history_item._picked_obj
            form.initial = {"text_input": history_item.search_text}
            template_context["history_item"] = history_item
    return render(request, "wordcounter/count_words.html", template_context)


@login_required
def show_history(request):
    search_history = WordCounterHistory.objects.filter(user=request.user).order_by("-created_at").all()
    return render(request, "wordcounter/history.html", {"search_history": search_history})
