from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfileinfo(models.Model):
    user = models.OneToOneField(User,
                                on_delete=models.CASCADE)

    # first_name = models.CharField(max_length=40)
    # last_name = models.CharField(max_length=40)
    # today_date = models.DateField(auto_now=True, auto_now_add=False)
    # User_age = models.DecimalField(max_digits=4, decimal_places=0)
    # User_email = models.EmailField(max_length=245)

# ADDITIONAL 
    portfolio_site = models.URLField(blank=True)

    profile_pic = models.ImageField(upload_to = 'Profile Pictures' , blank=True)

    def __str__(self): 
        return self.user.username