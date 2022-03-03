from django.db import models
from  django.contrib.auth.models import User

# Create your models here.
class Board(models.Model):
    name=models.CharField(max_length=30, unique=True)
    description=models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name

class Topic(models.Model):
    subject=models.CharField(max_length=255)
    last_updated=models.DateTimeField(auto_now_add=True)
    starter= models.ForeignKey(User,on_delete=models.CASCADE, related_name='topic')
    board=models.ForeignKey(Board,on_delete=models.CASCADE,related_name='topic')

class Post(models.Model):
    message= models.TextField(max_length=2000)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(null=True)
    created_by=models.ForeignKey(User,on_delete=models.CASCADE, related_name='posts')
    topic=models.ForeignKey(Topic,on_delete=models.CASCADE, related_name='posts')
    updated_by=models.ForeignKey(User,null=True,on_delete=models.CASCADE,blank=True,related_name='+')



