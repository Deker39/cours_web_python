from django.db.models import *
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

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


class ProductImage(Model):
    product = ForeignKey(Product, on_delete=CASCADE, related_name='image')
    image = ImageField(upload_to='products/')


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, *args, **kwargs):
        user = self.model(email=email, **kwargs)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password=None, *args, **kwargs):
        kwargs.setdefault('is_staff', True)
        kwargs.setdefault('is_superuser', True)
        return self.create_user(email, password, **kwargs)


class User(AbstractBaseUser):
    email = EmailField(unique=True, max_length=25)
    first_name = CharField(max_length=50)
    last_name = CharField(max_length=50)
    is_active = BooleanField(default=True)
    is_staff = BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        return self.email


