import re

pattern = re.compile(r'^[A-Za-z0-9$%#@]{8,}$')

password = 'Algarabali$%'

its_good_password = pattern.search(password)

if its_good_password:
    print("The password is valid")
else:
    print('Try again')