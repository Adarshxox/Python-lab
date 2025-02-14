import re

# wap to validate the mobile number

# length 10               +91   ?[6789][0-9]{9}

mobile_number = "+91 7025321186"

pattern = r'^(?:\+91\s|91\s)?[6789][0-9]{9}$'

result = re.match(pattern,mobile_number)

if result:

    print("Valid")

else:

    print("Not Valid")