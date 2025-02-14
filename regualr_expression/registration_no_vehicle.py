import re

text = "kl 09 ar 5675"

pattern = r'^kl\s[0-9]{2}\s[a-z]{1,2}\s[0-9]{4}$'

result = re.match(pattern,text)

if result:

    print("validated")

else:

    print("not valid")