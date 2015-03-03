from django.db import models


class LogEntry(models.Model):
    time    = models.DateTimeField(auto_now_add=True)
    level   = models.CharField(max_length=16)
    message = models.TextField()


class LogTag(models.Model):
    tag         = models.CharField(max_length=64)
    log_entries = models.ManyToManyField(LogEntry)

