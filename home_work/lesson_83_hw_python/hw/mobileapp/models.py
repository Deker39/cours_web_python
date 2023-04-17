from django.db.models import *


class ValueMobileAppReview(Model):
    nick = CharField(max_length=100)
    email = CharField(max_length=100)
    amount_star = IntegerField()
    describe = CharField(max_length=100)

    def __str__(self):
        return self.nick


