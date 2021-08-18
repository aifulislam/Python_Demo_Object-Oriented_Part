# 10/01/2021-----------
# Tamim Shahriar Subeen----
# Object Oriented Programming----------
# Module and Pakage-------

import builtins
p = dir(builtins)
print(p)

# Standard Library----------
# pi--------
import math
p = math.pi
print(p)

# pow()------
import math
p = math.pow(2, 3)
print(p)

# sqrt()------
import math
p = math.sqrt(25)
print(p)

# celi()------
import math
p = math.ceil(5.59)
print(p)

# floor()------
import math
p = math.floor(5.59)
print(p)

# datetime----------
import datetime
today = datetime.date.today()
print(today)

# datetime-------------
import datetime
today = datetime.datetime.today()
print(today)

# datetime-------------
from datetime import date
today = date.today()
print(today)

# datetime------------
from datetime import datetime
today = datetime.today()
print(today)

# webbrowser----------
import webbrowser
url = "http://abzoon.com"
webbrowser.open(url)

# webbrowser-------
import webbrowser
url = "http://subeen.com"
print(url)

# webbrowser-------
import webbrowser as wb
url = "http://abzoon.com"
print(url)


# Making New Module--------
def find_fib(n):
    if n <= 2:
        return 1
    fib_x, fib_next = 1, 1
    i = 3

    while i <= n:
        i += 1
        fib_x, fib_next = fib_next, fib_x + fib_next
        return fib_next
    for x in range(1, 11):
        print(find_fib(x))


