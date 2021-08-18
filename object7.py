# 20/01/2021-----------
# Tamim Shahriar Subeen----
# Object Oriented Programming----------
# Requests Module and Making File-------------

fp = open("test.txt", "w")
fp.write("This file was created using python!")
print(35)
fp.close()

# More using file & expansion---------
lines = ["This is first line.", "This is second line.", "This is third line"]
with open("file.txt", "w") as fp:
    for line in lines:
        fp.write(line+"\n")

# More using file & expansion---------
with open("file.txt", "r") as fp:
    content = fp.read()
    print(content)

# More using file & expansion---------
with open("text1.txt", "w") as fp:
    for line in lines:
        fp.write(line+"\n")

# More using file & expansion---------
with open("text1.txt", "r") as fp:
    for line in lines:
        print(line+"\n")

# More using file & expansion---------
with open("text1.txt", "r") as fpa:
    content = fpa.read()
    print(content)

# More using file & expansion---------
with open("text1.txt", "r") as fps:
    lines = fps.readlines()
    print(lines)
    for line in lines:
        print(line)

# More using file & expansion---------
with open("text1.txt", "r") as fpd:
    for line in fpd:
        print(line)


# Handel of access-----------
def div(a, b):
    try:
        return a/b
    except ZeroDivisionError:
        print("can't divide by zero")
    except TypeError:
        print("Unsupported type. Did you use string?")


print(div(10, 2))
print(div(3, 0))
print(div(9, 3))
print(div("12", 3))

# Handel of access-----------
import io
filename = "test1.txt"
mode = "r"
try:
    with open(filename, mode) as fp:
        content = fp.read()
        print(content)
except FileNotFoundError:
    print(filename, "not found. Please check if the file's name is correct.")
except io.UnsupportedOperation:
    print("Are you sure", filename, "is readable?")

'''
try:
    code...............
except Exception as e:
    print(e)
'''
# -----------End---------------#
