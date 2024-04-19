from django.db import models
from django.contrib.auth.models import AbstractBaseUser

class User(AbstractBaseUser):
    avatar = models.ImageField(null = True)
    

class BaseModel(models.Model):
    created_date = models.DateField(auto_now_add=True, null=True)
    updated_date = models.DateField(auto_now=True, null=True)

    class Meta:
        abstract = True

class Post(BaseModel):
    content =models.TextField()
    userID = models.ForeignKey(User, on_delete=models.CASCADE)

class Comment(BaseModel):
    content = models.CharField(max_length=200)
    userID = models.ForeignKey(User, on_delete=models.CASCADE)
    postID = models.ForeignKey(Post, on_delete=models.CASCADE)

class Group(BaseModel):
    name = models.CharField(max_length=200)
    description = models.TextField()
    userID = models.ForeignKey(User, on_delete=models.CASCADE)

class Membership(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    is_admin = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} in {self.group.name}"
    
class Survey(BaseModel):
    title = models.CharField(max_length=200)
    description = models.TextField()
    userID = models.ForeignKey(User, on_delete=models.CASCADE)

class Respone(BaseModel):
    surveyID = models.ForeignKey(Survey, on_delete=models.CASCADE)
    responedent = models.ForeignKey( User, on_delete=models.CASCADE)

class Question(BaseModel):
    questionText = models.TextField()
    surveyID = models.ForeignKey(Survey,on_delete=models.CASCADE)

class answer(models.Model):
    responeID = models.ForeignKey(Respone, on_delete=models.CASCADE)
    questionID = models.ForeignKey(Question, on_delete=models.CASCADE)
    
    

    


    


    
# Create your models here.
