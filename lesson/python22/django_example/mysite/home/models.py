from django.db.models import Model, CharField, IntegerField, GenericIPAddressField, URLField, UUIDField, JSONField


class User(Model):
    name = CharField(max_length=20)
    age = IntegerField()
    phone = CharField(max_length=20, null=True, blank=False)

