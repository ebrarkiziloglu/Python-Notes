# Conditionals

## Question 1
A leap year is a calendar year that contains an additional day added to keep the calendar year synchronized with the astronomical year. In the Gregorian calendar, each leap year has 366 days instead of 365, by extending February to 29 days rather than the common 28.
These extra days occur in each year which is an integer multiple of 4, except for the years evenly divisible by 100, but not by 400. Given a year between 1 and 10000, you will write a function that find whether it is a leap year or not.
  
  |  INPUT | OUTPUT |
| :------: | :------: |
| 1005 | not a leap year |
| 4 | leap year |
| 1000 | not a leap year |
| 4000 | not a leap year |

## Question 2
In mathematics, the greatest common divisor (GCD) of two or more integers is the largest positive integer that divides each of the integers. For two integers x, y, the greatest common divisor of x and y is denoted by gcd(x,y).
For example, gcd(8,12)=4. Without using recursion, write a function that finds GCD of two given integers.

  |  INPUT | OUTPUT |
| :------: | :------: |
| 14, 21 | 7 |
| 1, 300 | 1 |
| 256, 16 | 16 |
| 109, 109 | 109 |

## Question 3
Given a list of integers, write a function that finds the maximum sum of the two consecutive integers of the list and print and return the sum and the index of the occurrence.

  |  INPUT | OUTPUT |
| :------: | :------: |
| [-1,-2,-3,-4,5,0] | max sum: 5 , index: 4 |
| [9,-2,6,-1,3,0] | max sum: 7 , index: 0 |
| [5,0,6,0,7,0,8] | max sum: 8 , index: 5 |

## Question 4
There is a bug moving along the points with integer coordinates on the coordinate system. The bug always starts at the Origin (0,0). At each second, the bug moves exactly 1 unit according to the input, which consists of the letters R, L, U, D, respectively implying Right, Left, Up, Down. Given such an input, write a function to give the latest position of the bug and the number of its movements. The input is case-sensitive and only the uppercase letters will be used. If the input is not valid, print "Input is not Valid".

  |  INPUT | OUTPUT |
| :------: | :------: |
| "R R L L U D D D D R R R L U D L R U D U L R D" | latest position: (2, -3) , number of movements: 23 |
| " R  D  L  U " | latest position: (0, 0) , number of movements: 4 |
| "R R U U D D D L L " | latest position: (0, -1) , number of movements: 9 |
| "R R UUUDDD" | Input is not Valid |


# For-Loop

## Question 1

Given an integer sequence, read and split them to a list. Then, seperate out even and odd integers and print them in two seperate lists.

| INPUT   | OUTPUT |
| ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 1 21 30 44 5 7 700 103 33 32 2 | odd numbers: [1, 21, 5, 7, 103, 33]<br />even numbers: [30, 44, 700, 32, 2] |
| 4 2 4 2 | odd numbers: []<br />even numbers: [4, 2, 4, 2] |

## Question 2

Given an integer list, calculate the sum of all even integers.

| INPUT   | OUTPUT |
| ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 1 21 30 44 5 7 700 103 33 32 2 | 808 |
| 41 30 52 7 10 89 92 | 184 |

# While-Loop

## Question 1

Write a function to calculate the factorial of a given integer n. If n is a negative number, print "invalid input". 

| INPUT   | OUTPUT |
| ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 0 | 1 |
| 6 | 720 |
| 11 | 39916800 |

## Question 2

Given two positive integers, find their greatest common divisor (GCD) using a while loop.

Note: If you don't want to use Brute force method in this problem, you can generate an [Euclidean algorithm](https://en.wikipedia.org/wiki/Euclidean_algorithm) implementation as well.

| INPUT   | OUTPUT |
| ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 1<br />101 | 1 |
| 5<br />51 | 1 |
| 47<br />47 | 47 |
| 666<br />666666 | 666 |

