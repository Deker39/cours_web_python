from django.db.models import Model, CharField, EmailField, ForeignKey, CASCADE, ManyToManyField, TextField, OneToOneField, DecimalField

# Create your views here.
# OneToMany, ManyToMany, ManyToOne, OneToOne

# class Author(Model):
#     name = CharField(max_length=30, blank=False, null=False)
#     email = EmailField()
#     books = ManyToManyField("Book")
#
#     def __str__(self):
#         return self.name
#
#
# class AuthorProfile(Model):
#     author = OneToOneField(Author, on_delete=CASCADE)
#     bio = TextField()
#
#
# class Book(Model):
#     title = CharField(max_length=30, blank=False, null=False)
#     # author = ForeignKey(Author, related_name='books', on_delete=CASCADE)
#
#     def __str__(self):
#         return self.title

class Product(Model):
    name = CharField(max_length=255)
    description = TextField()
    price = DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.name