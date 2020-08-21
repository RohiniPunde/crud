from django.db import models
from django.core.validators import RegexValidator
import datetime

class Customer(models.Model):
    alphanumeric = RegexValidator(r'^[a-zA-Z]*$', 'Only alphanumeric characters are allowed.')
    name=models.CharField(max_length=200,null=True,validators=[alphanumeric])
    phone=models.BigIntegerField(null=True)
    email=models.EmailField(max_length= 200,null=True)
    #date_created= models.DateField()
   # date_created = models.DateField(_("date_created"),default=datetime.date.today)

    def __str__(self):
        return str(self.name)
