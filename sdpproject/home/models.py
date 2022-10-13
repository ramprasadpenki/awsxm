
from django.db import models

class info_request(models.Model):
    name=models.CharField(max_length=255)
    phone=models.CharField(max_length=10)
    bloodgroup=models.CharField(max_length=255)
    reason= models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    objects=models.Manager()


class donate(models.Model):
    name=models.CharField(max_length=255)
    phone=models.CharField(max_length=10)
    bloodgroup=models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    objects=models.Manager()

class Customer(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=500)
    role=models.CharField(max_length=50,default='0000000', editable=False)

    def register(self):
        self.save()

    @staticmethod
    def get_customer_by_username(username):
        try:
            return Customer.objects.get(username = username)
        except:
            return False

    def isExists(self):
        if Customer.objects.filter(email = self.email):
            return True

        return False