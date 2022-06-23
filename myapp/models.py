from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
class StoreDatabse(models.Model):
    store_code = models.CharField(max_length=300)

    bill_date = models.DateTimeField(null=True, blank=True)
    bill_no = models.IntegerField(blank=True,null=True)
    item_count = models.IntegerField(blank=True,null=True)
    sale_amount = models.DecimalField(max_digits=10,decimal_places=2)
    
    
@receiver(post_save,sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender,instance=None,created=False,**kwargs):
    if created:
        Token.objects.create(user=instance)