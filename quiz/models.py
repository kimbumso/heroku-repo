from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class Quiz(models.Model):
    title = models.CharField(max_length=200)
    content = RichTextUploadingField(blank=True, null=True)
    answer = models.IntegerField()
