from django.db.models import *
import random
import string


class User(Model):
    first_name = CharField(max_length=255)
    last_name = CharField(max_length=255)
    email = CharField(max_length=255)
    password = CharField(max_length=255)
    date_create = DateTimeField(auto_now=True)


class CatalogProduct(Model):
    title = CharField(max_length=255)


class Product(Model):
    title = CharField(max_length=255)
    price = DecimalField(max_digits=10, decimal_places=2)
    genre = CharField(max_length=255)
    developer = CharField(max_length=255)
    platform = CharField(max_length=255)
    language = CharField(max_length=255)
    description = CharField(max_length=255)
    main_image = ImageField(upload_to='shop/')
    catalog = ForeignKey(CatalogProduct, on_delete=CASCADE, related_name='catalog')


class ProductSystemRequirement(Model):
    products = ForeignKey(Product, on_delete=CASCADE, related_name='product')
    operating_system = CharField(max_length=255)
    processor = CharField(max_length=255)
    ram = CharField(max_length=255)
    video_card = CharField(max_length=255)
    free_hard_disk_space = CharField(max_length=255)


class ProductKey(Model):
    products = ForeignKey(Product, on_delete=CASCADE, related_name='p_key')
    key = CharField(max_length=255)

    def generate_rand_ket(self):
        self.total_cost = ''.join(random.choice(string.ascii_letters + string.digits) for i in range(10)).upper()
        self.save()


class ProductPhoto(Model):
    products = ForeignKey(Product, on_delete=CASCADE, related_name='image')
    image = ImageField(upload_to='shop/')


class CommentProduct(Model):
    auth = ForeignKey(User, on_delete=CASCADE, related_name='auth')
    product = ForeignKey(Product, on_delete=CASCADE, related_name='products')
    content = CharField(max_length=100)
    date = DateTimeField(auto_now=True)


class Order(Model):
    user = ForeignKey(User, on_delete=CASCADE, related_name='user')
    total_cost = DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    complete = BooleanField(default=False)
    quantity = IntegerField(default=0)
    date_order = DateTimeField(auto_now=True)

    def calculate_total_cost(self):
        total_cost = self.orderslist_set.aggregate(total=Sum('product__price'))['total']
        self.total_cost = total_cost or 0
        self.save()


class OrdersList(Model):
    order = ForeignKey(Order, on_delete=CASCADE, related_name='order')
    product = ForeignKey(Product, on_delete=CASCADE, related_name='p')


class ProductsDay(Model):
    product = ForeignKey(Product, on_delete=CASCADE, related_name='prod')
