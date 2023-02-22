from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class CustomerUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.SET_NULL, related_name= 'customeruser', blank=True, null=True)
    name = models.CharField(max_length=250, null=True)
    email = models.EmailField(max_length=254, null=True)

    def __str__(self):
        return self.name
    
class CategoryProduct(models.Model):
    name = models.CharField(max_length=250, null=True)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    discount_price = models.DecimalField(max_digits=7, decimal_places=2)
    digital = models.BooleanField(default=False, null=True, blank=False)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
    
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url
    
class CategoryOrder(models.Model):
    customer = models.ForeignKey(CustomerUser, on_delete=models.SET_NULL, blank=True, null=True)
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
    
class CategoryOrderItem(models.Model):
    product = models.ForeignKey(CategoryProduct, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(CategoryOrder, on_delete=models.SET_NULL, blank=True, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total
    
class CategoryShippingAddress(models.Model):
    customer = models.ForeignKey(CustomerUser, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(CategoryOrder, on_delete=models.SET_NULL, blank=True, null=True)
    address = models.CharField(max_length=250, null=True)
    city = models.CharField(max_length=250, null=True)
    state = models.CharField(max_length=250, null=True)
    name = models.CharField(max_length=250, null=True)
    zipcode = models.CharField(max_length=250, null=True)

    def __str__(self):
        return self.address