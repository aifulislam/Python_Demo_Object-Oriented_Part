# 20/01/2021-----------
# Tamim Shahriar Subeen----
# Data Structure & Algorithm----------
# Time & Space Complexity------

f_n = 10
f_s = 20
result = f_n + f_s
print(result)

# Time & Space Complexity------
n = input("Enter any number: ")
n = int(n)
result = n * (n + 1) / 2
print(result)

# Time & Space Complexity------O(n1)-----
n = input("Enter any number: ")
n = int(n)
result = 0
for i in range(1, n + 1):
    result = result + i
print(result)

# Time & Space Complexity-----O(n1)----
n = input("enter ny number: ")
n = int(n)

if n % 2 == 0:
    print(n, "is even number")
else:
    print(n, "is odd number")

# Time & Space Complexity------O(n1)----
n = 100
even = [False] * (n + 1)
for i in range(0, n + 1, 2):
    even[i] = True

print(even[4])
print(even[5])
print(even[-6])

# Time & Space Complexity----O(n2)----
n = input("Enter any number: ")
n = int(n)

count = 0

for i in range(n):
    for j in range(n):
        count += 1

print("n = ", n, "count = ", count)

# Time & Space Complexity-----O(n1)--
n = input("Enter any number: ")
n = int(n)

count = 0

for i in range(n):
    count += 1

print("n = ", n, "count = ", count)

# Time & Space Complexity----O(n3)----
n = input("Enter any number: ")
n = int(n)

count = 0

for i in range(n):
    for j in range(n):
        for k in range(n):
            count += 1

print("n = ", n, "count = ", count)

# Time & Space Complexity----O(n2)----
n = input("Enter any number: ")
n = int(n)

count = 0

for i in range(n):
    count += 1

for i in range(n):
    for j in range(n):
        count += 1

print("n = ", n, "count = ", count)

# -------Time & Space Complexity------#
# -----------End----------------------#


# Method of code testing--------
def average(L):
    if not L:
        return None

    return sum(L) / len(L)


if __name__ == "__main__":
    L = [1, 2, 3, 4, 5]
    print(average(L))


# Method of code testing--------
def average(L):
    if not L:
        return None

    return sum(L) / len(L)


if __name__ == "__main__":
    L = [1, 2, 3, 4, 5]
    expected_result = 3.0
    result = average(L)

    if expected_result == result:
        print("test passed")
    else:
        print("test failed!", "recived:", result, "expected:", expected_result)

# Using assert-----------




