import re
m =re.match(".*", "hellohello")
print(type(m))
if m is not None:
    print("matched")
if isinstance(m, re.Match):
    print("matched")

