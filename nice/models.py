from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.


class Korean(models.Model):
    title = models.CharField(max_length = 100)
    pub_date = models.DateTimeField('date published')
    image = models.ImageField(upload_to = 'kimage/', blank = True, null = True)
    body = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    sex = models.CharField(max_length = 50)
    interest = models.CharField(max_length = 10)
    nation = models.CharField(max_length = 50)
    region = models.CharField(max_length = 50)

    def __str__(self):
        return self.title
    
    def sum(self):
        return self.body[:40]

class Lforeigner(models.Model):
    title = models.CharField(max_length = 100)
    pub_date = models.DateTimeField('date published')
    image = models.ImageField(upload_to = 'lfimage/', blank = True, null = True)
    body = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    sex = models.CharField(max_length = 50)
    interest = models.CharField(max_length = 10)
    nation = models.CharField(max_length = 50)
    region = models.CharField(max_length = 50)

    def __str__(self):
        return self.title
    
    def sum(self):
        return self.body[:40]

class Sforeigner(models.Model):
    title = models.CharField(max_length = 100)
    pub_date = models.DateTimeField('date published')
    image = models.ImageField(upload_to = 'sfimage/', blank = True, null = True)
    body = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    sex = models.CharField(max_length = 50)
    interest = models.CharField(max_length = 10)
    nation = models.CharField(max_length = 50)
    region = models.CharField(max_length = 50)

    def __str__(self):
        return self.title
    
    def sum(self):
        return self.body[:40]


class K_Comment(models.Model):
    korean = models.ForeignKey(Korean, on_delete = models.CASCADE, null = True, related_name = 'kcomment')
    kcontents = models.TextField()

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.kcontents

class Lf_Comment(models.Model):
    lforeigner = models.ForeignKey(Lforeigner, on_delete = models.CASCADE, null = True, related_name = 'lfcomment')
    lfcontents = models.TextField()

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.lfcontents

class Sf_Comment(models.Model):
    sforeigner = models.ForeignKey(Sforeigner, on_delete = models.CASCADE, null = True, related_name = 'sfcomment')
    sfcontents = models.TextField()

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.sfcontents

