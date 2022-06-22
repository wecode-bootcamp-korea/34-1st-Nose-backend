import json
import bcrypt

from django.http import JsonResponse
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