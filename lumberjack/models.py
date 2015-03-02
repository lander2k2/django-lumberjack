from django.db import models

class LogEntry(models.Model):
    time    = models.DateTimeField(auto_now_add=True)
    level   = models.CharField(max_length=16)
    tag     = models.CharField(max_length=32)
    message = models.TextField()

