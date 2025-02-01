from datetime import timedelta

from django.db.models import Model, CharField, DateTimeField, ForeignKey, CASCADE, IntegerField
from django.utils import timezone


class Question(Model):
    question_text = CharField(max_length=200)
    pub_date = DateTimeField("date published")

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - timedelta(days=1)


class Choice(Model):
    question = ForeignKey(Question, on_delete=CASCADE)
    choice_text = CharField(max_length=200)
    votes = IntegerField(default=0)

    def __str__(self):
        return self.choice_text
