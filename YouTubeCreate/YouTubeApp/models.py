from django.db import models

# Create your models here.
from django.db import models
import datetime
from django.utils import timezone

class Comment(models.Model):
    comment_content = models.CharField(max_length=250)
    video_id = models.CharField(max_length=200)
    like = models.IntegerField(default=0)
    dislike = models.IntegerField(default=0)

class Reply(models.Model):
    comment = models.ForeignKey(Comment, null=True, blank=True, on_delete=models.PROTECT)
    reply_content = models.CharField(max_length=250)



