from datetime import timedelta

from django.db.models import Model, CharField, DateTimeField, ForeignKey, CASCADE, IntegerField
from django.utils import timezone
from django.contrib.admin import display


class Question(Model):
    question_text = CharField(max_length=200)
    pub_date = DateTimeField("date published")

    def __str__(self):
        return self.question_text

    @display(
        boolean=True,
        ordering="pub_date",
        description="Published recently?",
    )
    def was_published_recently(self):
        now = timezone.now()
        return now - timedelta(days=7) <= self.pub_date <= now


class Choice(Model):
    question = ForeignKey(Question, on_delete=CASCADE)
    choice_text = CharField(max_length=200)
    votes = IntegerField(default=0)

    def __str__(self):
        return self.choice_text
