import json
import bcrypt
import jwt

from django.http import JsonResponse
from django.views import View

from django.conf import settings
from users.models import User

class SignInView(View) :
    def post(self, request) :
        try:
            data          = json.loads(request.body)
            user_account  = data["account"]
            user_password = data["password"]

            user            = User.objects.get(account = user_account)
            hashed_password = user_password.encode("utf-8") 
            saved_password  = user.password.encode("utf-8")

            if not bcrypt.checkpw(hashed_password, saved_password):
                return JsonResponse({"message": "INVALID_USER"}, status=401)

            access_token = jwt.encode({"user_id": user.id}, settings.SECRET_KEY , settings.ALGORITHM)
            
            return JsonResponse({"message": "SUCCESS", "access_token": access_token}, status=200)

        except KeyError:
            return JsonResponse({"message": "KEY_ERROR"}, status=400)

        except User.DoesNotExist:
            return JsonResponse({"message": "INVALID_USER"}, status=400)