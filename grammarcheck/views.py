from django.shortcuts import render, get_object_or_404
from .forms import GrammarCheckForm
from .helpers import check_grammar as check_grammar_helper
from .models import GrammarCheckHistory
from django.contrib.auth.decorators import login_required


@login_required
def check_grammar(request, id=None):
    if request.method == "POST":
        form = GrammarCheckForm(request.POST)
        grammar_suggestions = check_grammar_helper(form.data["text_input"])
        suggestions = []
        for suggestion in grammar_suggestions:
            context = form.data["text_input"].split("\n")[suggestion.fromy]
            incorrect_segment = context[suggestion.fromx: suggestion.tox]
            context = context[:suggestion.fromx] + "<mark>{}</mark>".format(incorrect_segment) + incorrect_segment[suggestion.tox:]
            suggestions.append({
                "msg": suggestion.msg,
                "context": context,
                "replacements": suggestion.replacements
            })
        if form.is_valid():
            history = GrammarCheckHistory()
            history_item = request.GET.get("id", None)
            history.user = request.user
            history.search_text = form.data["text_input"]
            if not request.POST.get("id"):
                history._picked_obj = suggestions
                history.save()
            return render(request, "grammarcheck/check_grammar.html",
                          {'form': form,
                           'grammar_suggestions': suggestions})
    else:
        form = GrammarCheckForm()
        template_context = {"form": form}
        if id:
            history_item = get_object_or_404(GrammarCheckHistory, id=id)
            form.initial = {"text_input": history_item.search_text}
            template_context["history_item"] = history_item
            if history_item._picked_obj:
                template_context["grammar_suggestions"] = history_item._picked_obj
    return render(request, "grammarcheck/check_grammar.html", template_context)


@login_required
def show_history(request):
    search_history = GrammarCheckHistory.objects.filter(user=request.user).order_by("-created_at").all()
    return render(request, "grammarcheck/history.html", {"search_history": search_history})
