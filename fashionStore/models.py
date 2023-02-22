from django.db import models
from multiselectfield import MultiSelectField
from django.contrib.auth.models import User


class Customer(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200)
    def __str__(self):
        return f"Customer: {self.name}"

class Subscription(models.Model):
    email = models.CharField(max_length=100)

    def __str__(self):
        return f"Subscription email: {self.email}"

    class Meta:
        ordering = ['id']

class Brand(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(blank=True, default="default_picture.jpg")
    favorite = models.BooleanField(default=False)
    description = models.TextField()

    def __str__(self):
        return f"Brand: {self.name}"

    class Meta:
        ordering = ['id']

class Category(models.Model):
    name = models.CharField(max_length=200, null=True)
    image = models.ImageField(blank=True, default="default_picture.jpg")
    description = models.TextField()
    def __str__(self):
        return f"Category: {self.name}"
    class Meta:
        ordering = ['id']

class Size(models.Model):
    SIZE_CHOICES = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
        ('XL', 'Extra Large'),
    )
    size = models.CharField(max_length=3, choices=SIZE_CHOICES) #MultiSelectField(choices=SIZE_CHOICES)
    def __str__(self):
        return f"Size: {self.size}"

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.FloatField() #models.PositiveIntegerField()
    image = models.ImageField(blank=True, default="default_picture.jpg")
    date = models.DateTimeField(auto_now=True, blank=False)
    sale = models.BooleanField(default=False)
    size = models.ManyToManyField(Size, blank=True) #models.ForeignKey(Size, on_delete=models.SET_NULL, null=True)
    tag = models.CharField(max_length=100, blank=True)
    percent = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"Product: {self.name}"

    class Meta:
        ordering = ['id']


class Order(models.Model):
    STATUS_CHOICES = (('PENDING', 'Pending'), ('PROCESSING', 'Processing'), ('SHIPPED', 'Shipped'),
                      ('DELIVERED', 'Delivered'), ('CANCELED', 'Canceled'))

    customer = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    shipping_name = models.CharField(max_length=100)
    shipping_address = models.CharField(max_length=200)
    shipping_city = models.CharField(max_length=100)
    shipping_state = models.CharField(max_length=100)
    shipping_zip = models.CharField(max_length=10)

    ordered_item = models.CharField(max_length=200, blank=True)
    payment_method = models.CharField(max_length=50)
    payment_date = models.DateTimeField(auto_now_add=True)
    transaction_id = models.CharField(max_length=100, blank=True)

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Order: {self.id}"

    class Meta:
        ordering = ['-created_at']
