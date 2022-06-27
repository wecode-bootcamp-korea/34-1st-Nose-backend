from django.views import View
from django.http  import JsonResponse

from products.models import MainImage, Product, ThumbNailImage

class ProductListView(View) :
    def get(self, request) :
        try:
            if request.GET.get("fragrance"):
                fragrance_id = request.GET["fragrance"]
                products     = Product.objects.filter(fragrances__id = fragrance_id)
            else :
                products = Product.objects.all()

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

        except Product.DoesNotExist:
            return JsonResponse({"message": "NONE_PRODUCT"}, status=400)