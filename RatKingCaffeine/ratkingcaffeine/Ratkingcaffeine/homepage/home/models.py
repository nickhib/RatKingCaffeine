from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class usercomments(models.Model):
	commenttext = models.CharField(max_length=280)
	username = models.CharField(max_length=50)
	thedate = models.DateField(auto_now_add=True, auto_now=False, blank=True)
	#class Meta
	#	abstract = True
	#	ordering =['username']
#class userprofile(usercomments):
#	discription = models.CharField(max_length=280)
	
	def __str__(self):
		return self.username + ' comment is '+ self.commenttext +': '+ str(self.thedate)
class products(models.Model):
        productid= models.IntegerField()
        productname=models.CharField(max_length=280)
        productcategory=models.CharField(max_length=280)
        productroast = models.CharField(max_length=280)
        price = models.IntegerField();
        def __str__(self):
                return self.productname + ' price is '+ str(self.price)

class userinformation(models.Model):
        u = models.OneToOneField(User, on_delete=models.CASCADE)
        phone_number=models.CharField(max_length =280)
        First_name=models.CharField(max_length =280)
        Last_name=models.CharField(max_length = 280)
        address = models.CharField(max_length=280)
        city = models.CharField(max_length=280)
        zipcode = models.IntegerField()

class address(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

