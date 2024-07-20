from django.db import models

class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=50)
    desc = models.CharField(max_length=500)
    published_date = models.DateField()


