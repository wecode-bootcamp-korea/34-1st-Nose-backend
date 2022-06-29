from django.views import View
from django.http  import JsonResponse

from products.models import Product, MainImage

class ProductDetailView(View):
    def get(self, request, product_id):
        try:
            product     = Product.objects.get(id=product_id)
            main_images = MainImage.objects.filter(product_id=product_id)

            perfume_item = {
                "product_id"   : product.id,
                "name"         : product.name,
                "price"        : product.price,
                "main_img_url" : [ main_image.main_page_img_url for main_image in main_images ]
            }

            return JsonResponse({"perfume_item": perfume_item}, status=200)

        except Product.DoesNotExist :
            return JsonResponse({"message": "NONE_PRODUCT"}, status=400)