from django.db import models
from django.utils import timezone

class Question(models.Model):
    enquete_title = models.TextField()
    enquete_slug = models.TextField()
    create_user = models.TextField()
    create_date = models.DateTimeField(default=timezone.now)
    del_flg = models.IntegerField(default=0)

class QuestionDetail(models.Model):
    enquete = models.ForeignKey(Question, on_delete=models.CASCADE)
    question_text = models.TextField()
    question_type = models.TextField()
    rank = models.IntegerField()
    del_flg = models.IntegerField(default=0)


# Create your models here.
