import re

#Username,
# Can contain only letters (a-z, A-Z), digits (0-9), and underscores (_).
# Must start with a letter.
# Length should be between 4 to 15 characters.

username = "Speedyrogue_86"

pattern = r'^[A-z][A-Za-z0-9_]{3,14}$'

result = re.match(pattern,username)

if result:

    print("Valid Username")

else:

    print("Not Valid Username")