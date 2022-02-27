
# mail validity using Regex


import re
email_codition="^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"
user_email=input('enter the email id: ')

if re.search(email_codition,user_email):
    print(" Right Email ")
else:
    print(" Wrong Email ")
