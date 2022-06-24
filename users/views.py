import json
import bcrypt
import jwt

from django.conf  import settings
from django.http  import JsonResponse
from django.views import View

from users.models import User
from users.validations import validate_email, validate_password, validate_account, validate_phone_number

class SignUpView(View):
    def post(self, request):
        try: 
            data         = json.loads(request.body)
            name         = data['name']
            account      = data['account']
            email        = data['email']
            phone_number = data['phone_number']
            password     = data['password']

            validate_account(account)
            validate_email(email)
            validate_phone_number(phone_number)
            validate_password(password)

            if User.objects.filter(account = account).exists() :
                return JsonResponse({"message" : "THIS_ACCOUNT_ALEADY_EXIST"}, status = 400)

            if User.objects.filter(phone_number = phone_number).exists() :
                return JsonResponse({"message" : "THIS_PHONE_NUMBER_ALEADY_EXIST"}, status = 400)
                
            if User.objects.filter(email = email).exists() :
                return JsonResponse({"message" : "THIS_EMAIL_ALEADY_EXIST"}, status = 400)

            encoded_password = password.encode("utf-8")
            secret_password  = bcrypt.hashpw(encoded_password, bcrypt.gensalt())
            decoded_password = secret_password.decode("utf-8") 

            User.objects.create(
            name          = name,  
            account       = account,      
            email         = email,
            phone_number  = phone_number, 
            password      = decoded_password
            )

            return JsonResponse({"message":"SUCCESS"}, status=201)

        except KeyError:
            return JsonResponse({"message":"KEY_ERROR"}, status=400)

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