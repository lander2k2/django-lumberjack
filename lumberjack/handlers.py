from logging import Handler
from .models import LogEntry

class DBHandler(Handler, object):

    def emit(self, record):
        LogEntry.create(level=record.levelname,
                        tag=record.tag,
                        message=record)

