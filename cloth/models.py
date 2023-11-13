# cloth/models.py

from django.db import models

class CustomerCL(models.Model):
    first_name = models.CharField(max_length=50, default=None, null=True)
    last_name = models.CharField(max_length=50, default='')
    email = models.EmailField(unique=True)
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
class TagCL(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(default='')

    def __str__(self):
        return self.name

class ProductCL(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(default='')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    tags = models.ManyToManyField(TagCL)

    def __str__(self):
        return self.name

class OrderCL(models.Model):
    customer = models.ForeignKey(CustomerCL, on_delete=models.CASCADE)
    product = models.ForeignKey(ProductCL, on_delete=models.CASCADE, default=-1)
    quantity = models.IntegerField(default=0)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    tags = models.ManyToManyField(TagCL)

    def __str__(self):
        return f"Order for {self.customer}: {self.product} (Quantity: {self.quantity})"
