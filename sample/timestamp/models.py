import datetime
import uuid
from django.db import models

# Create your models here.


class MyUUIDModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    ct = datetime.datetime.now()
    uid = uuid.uuid4()

    apiObject = {ct: uid}

    print(apiObject)



    # Printing random id using uuid1()
    # print("The random id using uuid1() is : ", end="")
    # print(uuid.uuid1())
    #
    # apiObject = {id: ts}



    # def __str__(self):
    #     return "%s %s " % (self.id, self.ts)
    # other fields


