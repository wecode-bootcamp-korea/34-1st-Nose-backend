import json

from django.views       import View
from django.http        import JsonResponse

from core.models        import TimeStampModel
from users.models       import User
from products.models    import ThumbNailImage
from carts.models       import Cart
from core.utils         import token_decorator

class CartView(View):
    @token_decorator
    def post(self, request):
        try:        
            data            = json.loads(request.body)
            quantity        = data['quantity']
            product_id      = data['product_id']
            user            = request.user

            Cart.objects.get_or_create(
                user            = user, 
                product_id      = product_id,
                quantity        = quantity
            )
            
            return JsonResponse ({'message':'SUCCESS'}, status=200)
        except KeyError:
            return JsonResponse ({'message':'KEY_ERROR'}, status=400)
        except User.DoesNotExist:
            return JsonResponse ({'message':'INVALID_USER'}, status=400)

    @token_decorator
    def get(self, request):
        try:
            user    = request.user
            carts   = Cart.objects.filter(user_id=user.id)
            
            results = []
            for cart in carts:
                results.append(
                    {
                    'product_id'   : cart.product.id,
                    'product_name' : cart.product.name,
                    'image_url'    : ThumbNailImage.thumb_nail_img_url,
                    'quantity'     : cart.quantity,
                    'cart_id'      : cart.id
                    }
                )

            return JsonResponse({'results': 'results'}, status=200)

        except KeyError:
            return JsonResponse({'message': 'KEY_ERROR'}, status=400)
        except ThumbNailImage.DoesNotExist:
            return JsonResponse({'message': 'NO_IMAGE'}, status=401) 

    @token_decorator
    def delete(self, request):
        try:
            user = request.user
            cart = Cart.objects.get(user_id=user.id)
            
            cart.delete()

            return JsonResponse({'message': 'NO_CONTENT'}, status=200)
        except Cart.DoesNotExist:
            return JsonResponse({'message': 'Cart.DoesNotExist'}, status=404)                  