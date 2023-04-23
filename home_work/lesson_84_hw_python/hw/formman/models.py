from django.db.models import *


class ValueFormMan(Model):
    first_name = CharField(max_length=100)
    middle_name = CharField(max_length=100)
    last_name = CharField(max_length=100)
    city = CharField(max_length=100)


