6.Write the function startEndVowels(word) which returns True if the word
starts and ends with vowels.

source code :

def startEndVowels(word):
    s="AaEeIiOoUu"
    if s.__contains__(word[0]) and s.__contains__(word[-1]) :
        return True
    else :
        return False
s=input("Enter a word : ")
if startEndVowels(s):
    print("Given word ",s,"starts and ends with Vowel")
else :
    print("Given word ", s, "not starts and ends with Vowel")

output:
Enter a word : India
Given word  India starts and ends with Vowel

7.Write a function check_duplicate(Lst) which returns True if a list Lst
contains duplicate elements. It should return False, if all the elements in the
list Lst are unique.

source code :

def check_duplicate(Lst) :
    if len(Lst) == len(set(Lst)):
        return False
    else:
        return True
l=[]
n =int(input('Enter the size of list : '))
print("Enter the elemnets : ")
for i in range(0,n) :
    s=input()
    l.append(s)
if  not check_duplicate(l) :
    print("List not contains duplicates")
else :
    print("List contains duplicates")

output:
Enter the size of list : 5
Enter the elemnets : 
2
5
1
4
1
List contains duplicates


8.Write a program to pass a list to a function. Calculate the total number of
positive and negative numbers from the list and then display the count in
terms of dictionary.

source code:

def cal_pos_neg(lst) :
    n=0
    p=0
    for i in range(0,len(lst)) :
        if lst[i] < 0 :
            n=n+1
        else :
            p=p+1
    dist={'No of postive Elemeents' : p,'No of negative elements' : n}
    print(dist)

l=[]
n =int(input('Enter the size of list : '))
print("Enter the elemnets : ")
for i in range(0,n) :
    s=int(input())
    l.append(s)
cal_pos_neg(l)


output :
Enter the size of list : 5
Enter the elemnets : 
2
-1
3
-9
-8
{'No of postive Elemeents': 2, 'No of negative elements': 3}



9.Write a program to create a customized exception SalaryNotInRangeError. If
the input salary is not be in the range 5000 and 50000, raise the exception
otherwise display the employee salary.

source code :

class SalaryNotInRangeError(Exception):
    def __init__(self, s):
        self.s = s
    pass


sal = eval(input("Enter the salary : "))
try:
    if not 5000 < sal < 50000:
        raise SalaryNotInRangeError(sal)
except:
    print("Salar is not in the range (5000,50000)")
else:
    print("Salary is in the range (5000,50000)")

output:
Enter the salary : 1000
Salar is not in the range (5000,50000)


10.Write a program to copy the contents of one file to another file.

source code :

with open("input.txt") as f:
    with open("out.txt", "w") as f1:
        for line in f:
            f1.write(line)


f=open("input.txt")
f1=f.read()
f=open("out.txt")
f2=f.read()
print(f1)
print(f2)

output:
hii this is tharun
hii this is tharun

11.
19.Write a program to perform the following operations on complex numbers
using class, object and constructor.
(a) Addition
(b) Subtraction
(c) Multiplication


source code :
class Complex:
    def __init__(self,r,i):
        self.r=r;
        self.i=i;
    def add(self,c1,c2):
        temp=Complex(0,0)
        temp.r=c1.r+c2.r
        temp.i=c1.i+c2.i
        print("Sum of two Complex numbers : ",temp.r,"+i",temp.i)
    def sub(self,c1,c2):
        temp = Complex(0, 0)
        temp.r = c1.r - c2.r
        temp.i = c1.i - c2.i
        print("Difference of two number : ",temp.r, "+i", temp.i)
    def multi(self,c1,c2):
        C1=complex(c1.r,c1.i)
        C2=complex(c2.r,c2.i)
        c3=C1*C2
        print("Multiplication of two number : ",c3.real,"+i",c3.imag)
print("Enter the real and imaginary part of complex number 1 : ")
r=int(input())
i=int(input())
c1=Complex(r,i)
print("Enter the real and imaginary part of complex number 2 : ")
r=int(input())
i=int(input())
c2=Complex(r,i)
c3=Complex(0,0)
c3.add(c1,c2)
c3.sub(c1,c2)
c3.multi(c1,c2)

output:
Enter the real and imaginary part of complex number 1 : 
3
2
Enter the real and imaginary part of complex number 2 : 
3
2
Sum of two Complex numbers :  6 +i 4
Difference of two number :  0 +i 0
Multiplication of two number :  5.0 +i 12.0


12.Write a program to implement single inheritance.
a. Create the parent class Circle. Initialise the constructor with the radius of
the circle.
b. Define the method get_radius() and calc_area() to know the radius and area
of the circle.
c. Create the child class named Cylinder. Initialise the value of the height
within the constructor and call the constructor of the parent class to initialise
the radius of the cylinder.
d. Finally, define the method Calc_area() in the class Cylinder to calculate the
area of the cylinder.
Note: Area of Cylinder = 2 * pi * radius * height

source code:


import math
class Circle:
    def __init__(self, r):
        self.r = r

    def get_radius():
        print("Radius = ", r)

    def calc_area():
        a = math.pi * r * r
        print("Area = ", a)


class Cylinder():
    def __init__(self, r, h):
        Circle.__init__(self, r)
        self.h = h

    def Calc_area(self):
        a = 2 * math.pi * r * h
        print("Area of the Cylinder : ",a)


r=int(input("Enter the radius of a cylinder : "))
h=int(input("Enter the height of a cylinder : "))
c=Cylinder(r,h)
c.Calc_area()

output :
Enter the radius of a cylinder : 5
Enter the height of a cylinder : 6
Area of the Cylinder :  188.49555921538757

