from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator,MinValueValidator
from PIL import Image
# Create your models here.


DISTRICT_CHOICES = (

('Chittagong','Chittagong'),
('Rangpur','Rangpur'),
('Rajshahi','Rajshahi'),
('Dhaka','Dhaka'),
('Jashore','Jashore'),
('Sylhet','Sylhet'),
('Dinajpur','Dinajpur'),
('Mymensingh','Mymensingh'),
('Comilla','Comilla'),
('Kushtia','Kushtia'),

)
GENDER_CHOICES=(
        ('Male','MALE'),
        ('Female','FEMALE'),
)      
class Customer(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=50)
    phone=models.CharField(max_length=13)
    locality=models.CharField(max_length=200)
    city=models.CharField(max_length=200)
    district=models.CharField(choices=DISTRICT_CHOICES,max_length=50)
    gender=models.CharField(choices=GENDER_CHOICES,max_length=50)
    

    def __str__(self):
     return str(self.id)
       

     




CATEGORY_CHOICES=(
('S','Seeds'),
('P','Pesticides'),
('F','Fertilizer'),

)

class Product(models.Model):
    title=models.CharField(max_length=100)
    selling_price=models.FloatField()
    description=models.TextField()
    brand=models.CharField(max_length=100)
    category=models.CharField(choices=CATEGORY_CHOICES,max_length=2)
    product_image=models.ImageField(upload_to='productimg')

    def __str__(self):
     return str(self.id)

class AddCart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)

    def __str__(self):
     return str(self.id)

@property
def total_cost(self):
    return self.quantity * self.product.selling_price


STATUS_CHOICES=(
('Accepted','Accepted'),
('Delivered','Delivered'),
('Cancel','Cancel'),

)

class Order(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)
    ordered_date=models.DateTimeField(auto_now_add=True)
    status=models.CharField(max_length=50,choices=STATUS_CHOICES,default='Pending')


@property
def total_cost(self):
    return self.quantity * self.product.selling_price





class Machinery(models.Model):
    title=models.CharField(max_length=100)
    rent_perday=models.IntegerField()
    description=models.TextField()
    brand=models.CharField(max_length=100)
    product_image=models.ImageField(upload_to='machineryimg')
    is_Available=models.BooleanField(default=True)

    def __str__(self):
     return str(self.id)


class Rent_Request(models.Model):

    user_id=models.IntegerField(null=True)
    product_id=models.IntegerField(null=True)
    product_name=models.CharField(max_length=50)
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    phone=models.CharField(max_length=50)
    message=models.TextField(blank=True)
    confirm=models.BooleanField(default=False)
    
   
    def __str__(self) :
        return self.name