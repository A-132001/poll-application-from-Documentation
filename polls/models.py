from email.policy import default
from pyexpat import model
from unittest.util import _MAX_LENGTH
from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length =1000)
    pub_time = models.DateTimeField("Published Time")
    def __str__(self):
        return self.question_text
    
    
class Choice(models.Model):
    question = models.ForeignKey(Question,on_delete = models.CASCADE)
    choice_text = models.CharField(max_length = 200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text
    
    
class TestModel(models.Model):
    name = models.CharField(max_length = 50)
    def __str__(self):
        return self.name

