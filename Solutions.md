## Question 1

```python

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
```

## Question 2
```python

def sum_of_evens(lst):
    result = 0
    for e in lst:
        if int(e) % 2 == 0:
            result += int(e)
    return result

  
m = input().split()
print(sum_of_evens(m))
```

## Question 3
```python

n = int(input())
result = 1
if n < 0:
    print("invalid input")
else:
    while(n > 0):
        result *= n
        n -= 1
    print(result)
```

## Question 4
```python

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
```
