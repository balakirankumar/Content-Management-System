# from email_validator import validate_email, EmailNotValidError
# email = "bala@ymail.com"
#
# try:
#   # Validate.
#   valid = validate_email(email)
#
#   # Update with the normalized form.
#   email = valid.email
#   print(email)
# except EmailNotValidError as e:
#   # email is not valid, exception message is human-readable
#   print(str(e))
import re


def validate(**args):
    email = True if len(re.findall("([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)",args.get('email'))) >= 1 else False
    password = True if  len(args.get('password')) >= 8 and any(i.isupper() for i in args.get('password')) and any(i.islower() for i in args.get('password')) else False
    fullname = True if len(args.get('fullname').split()) >= 2 else False
    phonenumber = True if isinstance(args.get('phonenumber'),int) and len(str(args.get('phonenumber'))) ==  10 else False
    pincode = True if isinstance(args.get('pincode'),int) and len(str(args.get('pincode'))) ==  6 else False

    return all((email,password,fullname,phonenumber,pincode))
