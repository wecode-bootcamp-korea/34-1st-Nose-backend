from django.views     import View
from django.http      import JsonResponse
from django.db.models import Q

from products.models  import Product, ThumbNailImage

class ProductListView(View) :
    def get(self, request) :
        try:
            fragrance_id = request.GET.get("fragrance")
            category_id  = request.GET.get("category")

            q= Q()

            if fragrance_id :
                q &= Q(fragrances__id = fragrance_id)
            
            if category_id :
                q &= Q(category = category_id)
            
            products = Product.objects.filter(q)

            perfume_list = [
                {
                    "product_id"    : product.id,
                    "name"          : product.name,
                    "price"         : product.price,
                    "thumbnail_img" : ThumbNailImage.objects.get(product_id=product.id).thumb_nail_img_url,
                    "tags"          : [ tag.name for tag in product.tags.all() ]
                } for product in products
            ]

            return JsonResponse({"perfume_list": perfume_list}, status=200)

        except ThumbNailImage.DoesNotExist:
            return JsonResponse({"message": "NONE_THUMB_NAIL_IMAGE"}, status=400)