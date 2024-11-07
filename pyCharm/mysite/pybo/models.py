from django.db import models

# Create your models here.
from django.db import models


class Question(models.Model):
    subject = models.CharField(max_length=200) # 질문 제목
    content = models.TextField() # 질문 내용
    create_date = models.DateTimeField() # 질문 작성 일시

    def __str__(self):
        return self.subject


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE) # 질문에 대한 답변
    content = models.TextField() # 답변의 내용
    create_date = models.DateTimeField() # 답변 작성 일시