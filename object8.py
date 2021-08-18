# 20/01/2021-----------
# Tamim Shahriar Subeen----
# Object Oriented Programming----------
# Regular Expression-------------

s = "Afganistan, America, Bangladesh, Canada, Denmark, England, Greenland," \
    " Iceland, Netherlands, New Zealand, Sweden, Switzerland"
countries = s.split(",")
print(countries)
li = [item for item in countries if item.endswith("land") or item.endswith("lands")]
print(li)

# Regular Expression-------------
import re
s = "Afganistan, America, Bangladesh, Canada, Denmark, England, Greenland," \
    " Iceland, Netherlands, New Zealand, Sweden, Switzerland"
li = re.findall(r'(\w+lands*)', s)
print(li)

# Regular Expression-------------
import re
match = re.search('Bangla', "Bangladesh")
print(match)
mg = match.group()
print(mg)

# Regular Expression-------------
import re
match = re.search('Bangla', 'Bangladesh')
print(match)
mc = match.group()
print(mc)

# Regular Expression-------------
match = re.search('desh', 'Bangladesh')
print(match)
mc = match.group()
print(mc)
print(match)
print(type(match))
if match is None:
    print(True)
else:
    print(False)

# Regular Expression-------------
import re
s = "Bangladesh"
match = re.search('.', s)
m = match.group()
print(m)

# Regular Expression-------------
match = re.search('B.n', s)
n = match.group()
print(n)

# Regular Expression-------------
match = re.search('B.n..', s)
o = match.group()
print(o)

# Regular Expression-------------
p = "Bangladesh is our homeland"
match = re.search('.............', p)
q = match.group()
print(q)

# Regular Expression-------------
import re
s = "Bangladesh is our homeland"
match = re.search('o\w\w', s)
q = match.group()
print(q)

# Regular Expression-------------
import re
s = "Bangladesh is our homeland"
match = re.search('B\w+h', s)
q = match.group()
print(q)

# Regular Expression-------------
import re
s = "Bangladesh is our homeland"
match = re.search('B.+h', s)
q = match.group()
print(q)

# Regular Expression-------------
import re
s = "Bangladesh is our homeland"
match = re.search('B.+?h', s)
q = match.group()
print(q)

# Regular Expression-------------
import re
text = "Phone number: 01725624076"
match = re.search('\d+', text)
q = match.group()
print(q)

# Regular Expression-------------
import re
text = "house number: 5, Phone number: 01725624076"
match = re.search('\d+', text)
q = match.group()
print(q)

# Regular Expression-------------
import re
text = "house number: 5, Phone number: 01725624076"
match = re.search('\d{11}', text)
q = match.group()
print(q)

# Regular Expression-------------
import re
text = "house number: 5, Phone number: 017 25624076"
match = re.search('\d{3}\s*\d{8}', text)
q = match.group()
print(q)

# Regular Expression-------------
import re
text = "house number: 5, Phone number: 017 25624076"
match = re.search('\d{3}\s?\d{8}', text)
q = match.group()
print(q)

# Regular Expression-------------
import re
text = "Multiple phone number, 01711111111, 01811111111, 01910101010, 00000000000 123-123"
result = re.findall(r'\d{3}\s*\d{8}', text)
print(result)

# Regular Expression-------------
import re
text = "Multiple phone number, 01711111111,01303762522, 01811111111, 01910101010, 00000000000 123-123"
result = re.findall(r'01[3456789]\s*\d{8}', text)
print(result)

# Regular Expression-------------
import re
be = "Bangla english bangla"
m = re.findall(r'english', be)
print(m)

en = re.findall(r'^english', be)
print(en)

en = re.findall(r'english$', be)
print(en)

ba = re.findall(r'^Bangla', be)
print(ba)

ba = re.findall(r'bangla$', be)
print(ba)

ba = re.findall(r'^Bangla', be, re.IGNORECASE)
print(ba)

ba = re.findall(r'Bangla$', be, re.I)
print(ba)

# Regular Expression-------------
with open("file1.txt", "r") as f:
    text = f.read()

    print(text)

text = 'Bangladesh is our country.\nBangla is our Mother tone.\nPython is a programming language.\n'
print(text)

# Regular Expression-------------
import re
mm = re.findall(r'^.*?$', text)
print(mm)

nn = re.findall(r'^.+?$', text, re.M)
print(nn)

s = "<li>Tamim</li><li>Shakib</li><li>Mahmudullah</li><li>Mominul</li>"
result = re.findall(r'<li>(.*?)</li>', s)
print(result)

m = '<li>Ariful Islam</li><li>Ayon</li><li>Rajon</li> <li>Nahid Hasan</li><li>Tamim Iqbal</li>'
result = re.findall(r'<li>(.+?)</li>', m)
print(result)

# Regular Expression-------------






