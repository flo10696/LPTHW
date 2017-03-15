import re

t = "adr-engl"
m = re.match("(.*)(\-)(.*)", t)

if m:
    print m.group(3)
else:
    print("not found")
