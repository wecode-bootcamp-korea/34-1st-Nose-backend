from django.views     import View
from django.http      import JsonResponse

from products.models  import Product, ThumbNailImage, MainImage

class ProductListView(View) :
    def get(self, request) :
        try:
            offset       = request.GET.get("offset", 0)
            limit        = request.GET.get("limit", 16)

            filter_set = {
                "fragrance" : "fragrances__name",
                "category"  : "category_id"
            }

            filter = {
                filter_set.get(key) : value for key, value in request.GET.items() if filter_set.get(key)
            }

            products = Product.objects.filter(**filter)[offset:offset+limit]

            perfume_list = [
                {
                    "product_id"    : product.id,
                    "name"          : product.name,
                    "price"         : product.price,
                    "thumbnail_img" : ThumbNailImage.objects.get(product_id=product.id).thumb_nail_img_url,
                    "tags"          : [ tag.name for tag in product.tags.all() ],
                    "category"      : [ fragrance.name for fragrance in product.fragrances.all()] + ["All"],
                } for product in products
            ]

            return JsonResponse({"perfume_list": perfume_list}, status=200)

        except ThumbNailImage.DoesNotExist:
            return JsonResponse({"message": "NONE_IMAGES"}, status=400)

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
