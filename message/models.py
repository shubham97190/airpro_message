from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.

class Message(models.Model):

    recipients  = models.JSONField(blank=True, null=True, default=list)
    subject     = models.CharField(max_length=512)
    body_html   = RichTextUploadingField(blank=True, null=True)

class UserEmail(models.Model):
    email = models.EmailField()