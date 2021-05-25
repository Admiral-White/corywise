import datetime
import uuid
from django.db import models

# Create your models here.


class MyUUIDModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    ts = datetime.datetime.now().timestamp()

    def __str__(self):
        return "%s %s " % (self.id, self.ts)
    # other fields


