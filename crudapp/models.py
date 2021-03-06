from django.db import models
from django.core.validators import RegexValidator
import django.core.validators
import datetime
from django.utils.translation import gettext_lazy as _, ngettext_lazy

class Customer(models.Model):
    numeric = RegexValidator(r'^[0-9]*$','Only numbers are allowed','invalid')
    alphanumeric = RegexValidator(r'^[a-zA-Z]*$', 'Only alphanumeric characters are allowed.','invalid')
    name=models.CharField(max_length=200,null=True,validators=[alphanumeric])
    phone=models.CharField(max_length=12,null=True,validators=[numeric])
    email=models.EmailField(max_length= 200,null=True)
    #date_created= models.DateField()
   # date_created = models.DateField(_("date_created"),default=datetime.date.today)

    def __str__(self):
        return str(self.name)
