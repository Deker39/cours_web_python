from django.db.models import *


class infoRestModel(Model):
    name = CharField(max_length=100)
    specialization = CharField(max_length=100)
    address = CharField(max_length=100)
    website = CharField(max_length=100)
    tel = CharField(max_length=100)
