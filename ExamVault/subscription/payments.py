from rave_python import Rave, RaveExceptions, Misc
import re


public = "FLWPUBK_TEST-645532d24e73e56cdf04a8292d7d15d4-X"
secret = "FLWSECK_TEST-1f3416a7a9063c640a15efac209f3a84-X"
rave = Rave(public, secret, usingEnv = False)


def validate_ugandan_phone_number(phone_number):
    # Remove any spaces or special characters from the phone number
    cleaned_number = re.sub(r'\s+|-', '', phone_number)
    
    # Check if the cleaned number matches the Ugandan phone number format
    if re.match(r'^07\d{8}$', cleaned_number):
        return True
    else:
        return False


# mobile payload
payload = {
  "amount": "5000",
  "email": "lokukuminga@gmail.com",
  "phonenumber": "0782407832",
  "redirect_url": "https://rave-webhook.com/receivepayment",
  "IP":""
}

try:
  res = rave.UGMobile.charge(payload)
  print(res)
  res = rave.UGMobile.verify(res["status"])
  print(res)

except RaveExceptions.TransactionChargeError as e:
  print(f'1 - {e.err}')
  print(f'2 - {e.err["flwRef"]}')

except RaveExceptions.TransactionVerificationError as e:
  print(e.err)
  print(f'3 - {e.err["errMsg"]}')
  print(f'4 - {e.err["txRef"]}')
