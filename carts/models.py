from django.db import models

from core.models import TimeStampModel
from users.models import User
from products.models import Product

class Cart(TimeStampModel) :
    quantity = models.IntegerField(default=1)
    user     = models.ForeignKey(User, on_delete=models.CASCADE)
    product  = models.ForeignKey(Product, on_delete=models.CASCADE)

    class Meta:
        db_table = "carts"
    