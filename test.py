import re

pattern = r'\w+'

text = 'This is String! yes, this is string. and 123 is number.'

x = re.findall(pattern, text)

print(x)