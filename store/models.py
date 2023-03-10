from django.db import models
from django.contrib.auth.models import User
from blog.models import Admin
# Create your models here.

#This is for showing something at the begining of the page of Home and shop
class Website(models.Model):
    user = models.ForeignKey(Admin, on_delete=models.SET_NULL, blank=True, null=True)
    header_title = models.CharField(max_length=150, null=True)
    title = models.CharField(max_length=250, null=True)
    text = models.TextField(max_length=300, null=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.title
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

#This is for products in shop page
class Shop(models.Model):
    name = models.CharField(max_length=250, null=True)
    price = models.FloatField()
    digital = models.BooleanField(default=False, null=True, blank=False)
    image = models.ImageField(null=True, blank=True)
    description = models.TextField(max_length=500, null=True)
    luxury = models.BooleanField(default=False, null=True, blank=False )
    luxury_1 = models.BooleanField(default=False, null=True, blank=False )
    luxury_2 = models.BooleanField(default=False, null=True, blank=False )



    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url
    
#This is for showing something at the begining of the page of shop
class Website_Shop(models.Model):
    user = models.ForeignKey(Admin, on_delete=models.SET_NULL, blank=True, null=True)
    header_title = models.CharField(max_length=150, null=True)
    title = models.CharField(max_length=250, null=True)
    text = models.TextField(max_length=300, null=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.title
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url
#finish showing ^^^^


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name = 'customer', null=True, blank=True)
    name = models.CharField(max_length=250, null=True)
    email = models.CharField(max_length=250, null=True)

    def __str__(self):
        return  self.name

class Product(models.Model):
    name = models.CharField(max_length=250, null=True)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    digital = models.BooleanField(default=False, null=True, blank=False)
    image = models.ImageField(null=True, blank=True)
    description = models.TextField(max_length=500, null=True)
    luxury = models.BooleanField(default=False, null=True, blank=False )

    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url
        

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False, null=True, blank=False)
    transaction_id = models.CharField(max_length=250, null=True)

    def __str__(self):
        return str(self.id)

    @property
    def shipping(self):
        shipping = False
        orderitems = self.orderitem_set.all()
        for i in orderitems:
            if i.product.digital == False:
                shipping = True
        return shipping   

    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total  = sum([item.get_total for item in orderitems])
        return total

    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total  = sum([item.quantity for item in orderitems])
        return total

class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total


class ShppingAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    address = models.CharField(max_length=250, null=True)
    city = models.CharField(max_length=250, null=True)
    state = models.CharField(max_length=250, null=True)
    name = models.CharField(max_length=250, null=True)
    zipcode = models.CharField(max_length=250, null=True)

    def __str__(self):
        return self.address
