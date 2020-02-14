from django.contrib import admin
from .models import GrammarCheckHistory


class GrammarCheckHistoryAdmin(admin.ModelAdmin):
    list_filter = ('user',)
    list_display = ('search_text', 'user', 'created_at',)


admin.site.register(GrammarCheckHistory, GrammarCheckHistoryAdmin)
