from django.db import models
from django.contrib.auth.models import User
from picklefield.fields import PickledObjectField


class GrammarCheckHistory(models.Model):
    search_text = models.TextField(blank=False)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    _picked_obj = PickledObjectField(blank=True, null=True)

    def __str__(self):
        return self.search_text[0:128]

    class Meta:
        verbose_name = "Grammar Check History"
        verbose_name_plural = "Grammar Check Histories"
