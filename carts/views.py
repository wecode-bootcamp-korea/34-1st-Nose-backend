import json

from django.views       import View
from django.http        import JsonResponse
from django.db.models   import F

from core.models        import TimeStampModel
from users.models       import User
from products.models    import Product
from carts.models       import Cart
from core.utils         import token_decorator

class CartView(View):
    @token_decorator
    def post(self, request):
        try:        
            data        = json.loads(request.body)
            quantity    = data['quantity']
            product_id  = data['product_id']
            user        = request.user

            cart,is_created = Cart.objects.get_or_create(
                user = user , product_id=product_id
            )
            cart.quantity = F('quantity') + quantity
            cart.save()
            
            return JsonResponse ({'message':'SUCCESS'}, status=200)
        except KeyError:
            return JsonResponse ({'message':'KEY_ERROR'}, status=400)
        except User.DoesNotExist:
            return JsonResponse ({'message':'INVALID_USER'}, status=400)