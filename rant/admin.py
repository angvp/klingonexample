from django import forms
from django.contrib import admin

from rant.models import Category, Rant
from klingon.admin import TranslationInline, TranslationInlineForm, create_translations


class RichTranslationInlineForm(TranslationInlineForm):
    widgets = {
        'CharField': forms.TextInput(attrs={'class': 'klingon-char-field'}),
        'TextField': forms.Textarea(attrs={'class': 'klingon-text-field'}),
        'SlugField': forms.TextInput(attrs={'readonly': 'readonly', 'disabled':
            'disabled'}),
    }


class RichTranslationInline(TranslationInline):
    form = RichTranslationInlineForm


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'translations_link')
    search_fields = ['name', 'description']
    inlines = [TranslationInline]
    actions = [create_translations]


class RantAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug', 'translations_link')
    search_fields = ['title', 'description']
    inlines = [RichTranslationInline]
    actions = [create_translations]


admin.site.register(Category, CategoryAdmin)
admin.site.register(Rant, RantAdmin)
