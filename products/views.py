from django.views import View
from django.http  import JsonResponse

from products.models import Product, ThumbNailImage

class ProductListView(View) :
    def get(self, request) :
        try:
            products = Product.objects.all()

            result  = [
                {
                    "product_id"    : product.id,
                    "name"          : product.name,
                    "price"         : product.price,
                    "thumbnail_img" : ThumbNailImage.objects.get(product_id=product.id).thumb_nail_img_url,
                    "tags"          : [ tag.name for tag in product.tags.all() ]
                } for product in products
            ]

            return JsonResponse({"perfume_list": result}, status=200)

        except Product.DoesNotExist:
            return JsonResponse({"message": "NONE_PRODUCT"}, status=400)