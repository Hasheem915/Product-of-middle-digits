num = int(input("Enter the number"))
x = num
numlen = 0

while x > 0:
  numlen = numlen + 1
  x = x // 10

if numlen >= 4:
  numlen = numlen // 2
  count = 0
  while num > 0:
    rem = num % 10
    if count == numlen:
      mid1 = rem

    elif count == (numlen - 1):
      mid2 = rem

    count = count + 1
    num = num // 10
  pro = mid1 * mid2

print("The product of the middle digits is", pro)
