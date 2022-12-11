# Q1: "Given an array of positive integers `nums`, return a list of all of the negative integers.
 nums = [1, 3, 5, 7, 8]

 for i in nums:
     print(-abs(i))


# Q2: "Given a string, return a list of all of the digits in the string.
address = "123 Real Street, Apt. 2, Springfield, OR 43498"

ans = [int(i) for i in address.split() if i.isdigit()]

print(str(ans))


# Q3: "Given a string `digits`, return a **string** of the digits + 1.

 digits = '123'
 digits2 = ' '

 for  d in digits:
     digits2.append(d + 1)

print(digits2)
   