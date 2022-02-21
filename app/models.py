from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
STATE_CHOICES = (
    ('Parbat & Sagarmatha','Parbat & Sagarmatha'),
    ('Karnali Pradesh','Karnali Pradesh'),
    ('Bagmati Pradesh','Bagmati Pradesh'),
    ('Surkhet','Surkhet'),
    ('Bara','Bara'),
    ('Rolpa','Rolpa'),
    ('Dolpa','Dolpa'),
    ('Putalisadak & Kamal Pokhari','Putalisadak & Kamal Pokhari'),
    ('Siraha and Saptari','Siraha and Saptari'),
    ('Kathmandu','Kathmandu'),
    ('Pokhara','Pokhara'),
    ('Biratnagar','Biratnagar'),
    ('Bardiya','Bardiya'),
    ('Madhesh','Pradesh'),
    ('Sikkim & Darjiling','Sikkim & Darjiling'),
    ('Kanchanpur','Kanchanpur'),
    ('Jhapa','Jhapa'),
    ('Chisapani','Chisapani'),
    ('Birtamod','Birtamod'),
    ('Tharu pradesh','Tharu pradesh'),
    ('Newari','Newari'),
    ('Bhaktapur','Bhaktapur'),
    ('Mahendranagar','Mahendranagar'),
    ('Tandi','Tandi'),
    ('Lamahi','Lamahi'),
    ('Narayanghat','Narayanghat'),
    ('Puducherry','Puducherry'),
    ('Aachami','Aachami'),
    ('Mustang','Mustang'),
    ('Manang','Manang'),
    ('Baitadi','Baitadi'),
    ('Nepaljung','Nepaljung'),
    ('Kritipur','Kritipur'),
    ('Thimi','Thimi'),
    ('Lumbini','Pradesh'),
    ('West Side','West Side'),
)
class Customer(models.Model):
 user = models.ForeignKey(User,on_delete=models.CASCADE)
 name = models.CharField(max_length=200)
 locality = models.CharField(max_length=200)
 city = models.CharField(max_length=50)
 zipcode = models.IntegerField()
 state = models.CharField(choices=STATE_CHOICES, max_length=50)

 def _str_(self):
  return str(self.id)

CATEGORY_CHOICES = (
 ('M', 'Mobile'),
 ('L', 'Laptop'),
 ('TW', 'Top Wear'),
 ('BW', 'Bottom Wear'),    
)
class Product(models.Model):
 title = models.CharField(max_length=100)
 selling_price = models.FloatField()
 discounted_price = models.FloatField()
 description = models.TextField()
 brand = models.CharField(max_length=100)
 category = models.CharField( choices=CATEGORY_CHOICES,max_length=2)
 product_image = models.ImageField(upload_to='productimg')

 def _str_(self):
  return str(self.id)


class Cart(models.Model):
 user = models.ForeignKey(User, on_delete=models.CASCADE)
 product = models.ForeignKey(Product, on_delete=models.CASCADE)
 quantity = models.PositiveIntegerField(default=1)

 def _str_(self):
  return str(self.id)


STATUS_CHOICES = (
  ('Accepted','Accepted'),
  ('Packed','Packed'),
  ('On The Way','On The Way'),
  ('Delivered','Delivered'),
  ('Cancel','Cancel')  
)

class OrderPlaced(models.Model):
 user = models.ForeignKey(User, on_delete=models.CASCADE)
 customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
 product = models.ForeignKey(Product, on_delete=models.CASCADE)
 quantity = models.PositiveIntegerField(default=1)
 ordered_date = models.DateTimeField(auto_now_add=True)
 status = models.CharField(max_length=50,choices=STATUS_CHOICES,default='Pending')   




