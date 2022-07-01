import json

from django.views       import View
from django.http        import JsonResponse

from users.models       import User
from products.models    import ThumbNailImage
from carts.models       import Cart
from core.utils         import token_decorator

class CartView(View):
    @token_decorator
    def post(self, request):
        try:        
            data       = json.loads(request.body)
            quantity   = data['quantity']
            product_id = data['product_id']
            user       = request.user
            
            cart, is_created  = Cart.objects.get_or_create(
                user          = user, 
                product_id    = product_id,
                defaults      = {
                    "quantity" : quantity
                }
            )

            if not is_created:
                cart.quantity += quantity

            cart.save()

            return JsonResponse ({'message':'SUCCESS'}, status=200)
        except KeyError:
            return JsonResponse ({'message':'KEY_ERROR'}, status=400)

    @token_decorator
    def get(self, request):
        try:
            user  = request.user
            carts = Cart.objects.filter(user_id=user.id)

            results = [{
                    'id'           : cart.product.id,
                    'itemName'     : cart.product.name,
                    'thumbnail_img': cart.product.thumbnailimage_set.get(product_id=cart.product.id).thumb_nail_img_url,
                    'quantity'     : cart.quantity,
                    'cart_id'      : cart.id,
                    'price'        : cart.product.price
                    } for cart in carts ]

            return JsonResponse({'results': results}, status=200)

        except ThumbNailImage.DoesNotExist:
            return JsonResponse({'message': 'NO_IMAGE'}, status=401) 

    @token_decorator
    def delete(self, request):
        try:
            user     = request.user
            cart_ids = request.GET.getlist('cart_id')

            carts    = Cart.objects.filter(id__in=cart_ids, user_id=user.id)

            if not carts:
                return JsonResponse({'message' : 'NOT_EXIST_CART'}, status=400)

            carts.delete()

            return JsonResponse({'message': 'DELETE_SUCCESS'}, status=201)
        
        except Cart.DoesNotExist:
            return JsonResponse({'message': 'CART_DOES_NOT_EXIST'}, status=405)                  