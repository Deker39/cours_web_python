from django.db.models import *
from django.core.exceptions import ValidationError


def validate_rating(value):
    if not 0 <= value <= 100:
        raise ValidationError('Value must be between 0 and 100.')


class ValueBookReview(Model):
    nick = CharField(max_length=100)
    rating = IntegerField(validators=[validate_rating])
    review = CharField(max_length=100)
    spoiler = BooleanField(default=False)

    def __str__(self):
        return self.nick


