from django.db.models import Model, CharField, IntegerField, DecimalField, ForeignKey, CASCADE


class Company(Model):
     name = CharField(max_length=50)


class Product(Model):
    company = ForeignKey(Company, on_delete=CASCADE)
    name = CharField(max_length=50)
    price = DecimalField(max_digits=15, decimal_places=2)
