# CONDITIONALS

## Question 1
def is_leap_year(x):
    if x % 4 == 0:
        if x % 100 == 0:
            if x % 400 == 0:
                print("leap year")
                return 1
            else:
                print("not a leap year")
                return 0
        else:
            print("leap year")
            return 1
    else:
        print("not a leap year")
        return 0

## Question 2
 def GCD(x, y):
    gcd = 1
    if x > y:
        least = y
    else:
        least = x
    for i in range(1, least + 1):
        if (x % i == 0) and (y % i == 0):
            gcd = i
    return gcd
 
## Question 3
def find_max_sum(lst):
    max_sum = -100
    index = -1
    prev = lst[0]
    n = len(lst)
    for i in range(1, n):
        if (prev+lst[i]) > max_sum:
            max_sum = (prev+lst[i])
            index = i-1
        prev = lst[i]
    print("max sum:", max_sum, ", index:", index)
    return max_sum, index
 
 ## Question 4
 def walking_along_coordinates(input_str):
    lst = input_str.split()
    movements = 0
    num_of_r = 0
    num_of_l = 0
    num_of_u = 0
    num_of_d = 0
    for e in lst:
        if e == "R":
            num_of_r += 1
            movements += 1
        elif e == "L":
            num_of_l += 1
            movements += 1
        elif e == "U":
            num_of_u += 1
            movements += 1
        elif e == "D":
            num_of_d += 1
            movements += 1
        else:
            print("Input is not Valid")
            return 0
    axis = num_of_r - num_of_l
    ordinate = num_of_u - num_of_d
    print("latest position:", (axis, ordinate), ", number of movements:", movements)
    return (axis, ordinate), movements

 ## Question 5
def tv_guide(age):
    if age > 17:
        print("This person can watch anything.")
    elif age > 12:
        print("This child can watch programs that are rated G or PG-13; but not NC-17.")
    else:
        print("This child can only watch programs that are rated G.")
    return


# FOR-LOOP

## Question 1
odd_list = []
even_list = []
m = input().split()
for e in m:
    x = int(e)
    if x % 2 == 0:
        even_list.append(x)
    else:
        odd_list.append(x)

print("odd numbers: ", odd_list)
print("even numbers: ", even_list)

## Question 2
def sum_of_evens(lst):
    result = 0
    for e in lst:
        if int(e) % 2 == 0:
            result += int(e)
    return result

  
m = input().split()
print(sum_of_evens(m))


# WHILE-LOOP

## Question 1
n = int(input())
result = 1
if n < 0:
    print("invalid input")
else:
    while(n > 0):
        result *= n
        n -= 1
    print(result)

## Question 2
x = int(input())
y = int(input())
if y > x:
    temp = y
    y = x
    x = temp
i = 1
res = 1
while i <= y:
    if x % i == 0 and y % i == 0:
        res = i
    i += 1

print(res)
