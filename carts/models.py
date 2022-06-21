from django.db import models

from core.models import TimeStampModel
from users.models import User
from products.models import Product

class Cart(TimeStampModel) :
    quatity    = models.CharField(max_length=10)
    user_id    = models.ForeignKey(User, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)

    class Meta:
        db_table = "carts"
    