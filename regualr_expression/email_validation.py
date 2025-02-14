import re

# wap to validate gmail id

# abc123.ab@gmail.com

gmail = "abc123.ab@gmail.com"

pattern = r'^[A-Za-z0-9._-]+@gmail.com$'

result = re.match(pattern,gmail)

if result:

    print("valid")

else:

    print("not valid")