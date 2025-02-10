from django.contrib.admin import TabularInline, ModelAdmin, site

from .models import Question, Choice


class ChoiceInline(TabularInline):
    model = Choice
    extra = 1


class QuestionAdmin(ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {
            'fields': ['pub_date'],
            # 'classes': ['collapse']
        }),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']


site.register(Question, QuestionAdmin)
