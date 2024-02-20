from django.db import models

# Create your models here.
class Product(models.Model):
    title=models.CharField(max_length=120)
    content=models.CharField(max_length=120)
    price=models.DecimalField(max_digits=7,decimal_places=2,default=99.99)

    def sale_price(self):
        return float("%.2f" %(float(self.price)*0.8))
    
    def discount_diff(self):
        return float(self.price)-self.sale_price()
    
    def __str__(self):
        return f"{self.id} --> {self.title}"