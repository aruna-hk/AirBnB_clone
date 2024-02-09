#!/usr/bin/python3
import re
#regex to match ditionary

with open("file.json", "r") as file:
    content = file.read()

pattern = r'\{[^{}]|(?R))*\}'
matchs = re.findall(pattern, content)
