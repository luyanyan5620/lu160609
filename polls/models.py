from django.db import models
from django.utils.encoding import python_2_unicode_compatible

# Create your models here.
@python_2_unicode_compatible
class Question(models.Model):
    context = models.CharField(max_length=200)
    pub_date =models.DateTimeField('date published')
    
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    
    def __str__(self):
        return self.context


@python_2_unicode_compatible
class Choice(models.Model):
    question = models.ForeignKey(Question,on_delete =models.CASCADE)
    #what's the mean of "on_delete =models.CASCADE)"
    choice_text =models.CharField(max_length=200)
    votes =models.IntegerField(default=0)
    
    def __str__(self):
       	return self.choice_text