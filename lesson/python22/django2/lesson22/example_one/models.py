from django.db.models import Model, CharField, IntegerField


class Person(Model):
    name = CharField(max_length=20)
    age = IntegerField()

