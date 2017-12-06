from django.db import models
import string
import random

def code_generator(size=6,chars=string.ascii_lowercase+string.digits):
    return ''.join(random.choice(chars) for _ in range(0,size))


# Create your models here.
class KirrURL(models.Model):
    url= models.CharField(max_length=200,)
    shortcode = models.CharField(max_length=15,unique=True)
    updated = models.DateTimeField(auto_now=True)  # everytime the model is saved
    timestamp=models.DateTimeField(auto_now_add=True)#when model was created


    def save(self, *args, **kwargs):
        print("hello")
        self.shortcode = code_generator()
        super(KirrURL,self).save(*args, **kwargs)

    def __str__(self):
        return str(self.url)