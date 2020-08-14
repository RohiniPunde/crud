from django.db import models

class Customer(models.Model):
    name=models.CharField(max_length=200,null=True)
    phone=models.CharField(max_length=200,null=True)
    email=models.CharField(max_length=200,null=True)
    date_created=models.DateTimeField(auto_now=True,null=True)

    def __str__(self):
        return str(self.name)
