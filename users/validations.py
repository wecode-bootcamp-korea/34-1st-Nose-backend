import re

from django.core.exceptions import ValidationError

def validate_account(value) :
    ACCOUNT_CHECK = "^[a-z0-9+_.]{4,}$"
    
    if not re.match(ACCOUNT_CHECK, value) :
        raise ValidationError("INVALID_ACCOUNT")

def validate_email(value) :
    EMAIL_CHECK =  "^[a-zA-Z0-9+_.]+@[a-zA-Z0-9-]+.[a-zA-Z]{2,3}$"

    if not re.match(EMAIL_CHECK, value) :
        raise ValidationError("INVALID_EMAIL")

def validate_phone_number(value) :
    NUMBER_CHECK = "^[0-9]{10,11}$"
    
    if not re.match(NUMBER_CHECK, value) :
        raise ValidationError("INVALID_NUMBER")

def validate_password(value) :
    PW_CHECK = "^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$"

    if not re.match(PW_CHECK, value) :
        raise ValidationError("INVALID_PASSWORD")