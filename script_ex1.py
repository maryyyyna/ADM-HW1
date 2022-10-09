# -*- coding: utf-8 -*-
"""
Created on Thu Sep 29 20:50:54 2022

@author: Marina
"""

#1-----Say "Hello, World!" With Python-----
print("Hello, World!")


#2-----Python If-Else-----
import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input().strip())
    if n%2 != 0:
        print("Weird")

    else:
        if 2<=n<=5:
            print("Not Weird")
        
        elif 6<=n<=20:
            print("Weird")
        
        else:
            print("Not Weird")
 
            
#3-----Arithmetic Operators-----
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    
    print(a+b)
    print(a-b)
    print(a*b)


#4-----Python: Division-----
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    
    if b > 0:
        print(a//b)
        print(a/b)

        
#5-----Loops-----
if __name__ == '__main__':
    n = int(input())
    
    for i in range(n):
        print(i**2)

        
#6-----Write a function-----
def is_leap(year):
    leap = False
    
    if year % 4 == 0:
        leap = True
        if year % 100 == 0:
            leap = False
            if year % 400 == 0:
                leap = True
    
    return leap
    
year = int(input())
print(is_leap(year))

#7-----Print Function-----
if __name__ == '__main__':
    n = int(input())
    s = ''
    for i in range(1,n+1):
        s += str(i)
    print(s)

    
#1-----List Comprehensions-----
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    result = [[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k != n]
    print(result)
    
#2-----Find the Runner-Up Score!-----
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    new_arr = sorted(set(arr))
    print(new_arr[-2])
    
    
#3-----Nested Lists-----
if __name__ == '__main__':
    records = []
    scores = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        
        records.append([name, score])
        if score not in scores:
            scores.append(score)
    
    sorted_scores = sorted(scores)
    second_lowest = sorted_scores[1]
    
    names = []
    for l in records:
        if l[1] == sorted_scores[1]:
            names.append(l[0])
    
    sorted_names = sorted(names)
    for name in sorted_names:
         print(name)
    
    
#4-----Finding the percentage-----
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    marks_list = student_marks[query_name]
    tot = 0
    for mark in marks_list:
        tot+=mark

    result = tot/len(marks_list)
    print("{:.2f}".format(result))

    
#5-----Lists-----
if __name__ == '__main__':
    N = int(input())
    result = []
    for _ in range(N):
        comand = input().split()
        if comand[0] == "insert":
            result.insert(int(comand[1]), int(comand[2]))
        
        elif comand[0] == "print":
            print(result)
        
        elif comand[0] == "remove":
            result.remove(int(comand[1]))
            
        elif comand[0] == "append":
            result.append(int(comand[1]))
            
            
        elif comand[0] == "sort":
            result.sort()
            
        elif comand[0] == "reverse":
            result.reverse()
            
        else:
            result.pop()
            
            
#6-----Tuples-----
if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())

    print(hash((tuple(integer_list))))


#1-----sWAP cASE-----
def swap_case(s):
    return s.swapcase()

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
    

#2-----String Split and Join-----
def split_and_join(line):
    # write your code here
    l = line.split()
    new_line = "-".join(l)
    return new_line
    
if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
    
    
#3-----What's Your Name?-----
def print_full_name(first, last):
    # Write your code here
    print("Hello " + first + " " + last + "! " + "You just delved into python.")


if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)
    
    
#4-----Mutations-----
def mutate_string(string, position, character):
    l = list(string)
    l[position] = character
    return ''.join(l)

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
    
    
#5-----Find a string-----
def count_substring(string, sub_string):
    n = len(sub_string)
    count = 0
    for i in range(0, len(string)):
        if string[i:i+n] == sub_string:
            count+=1
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
    
    
#6-----String Validators-----
if __name__ == '__main__':
    s = input() 
line1 = False
line2 = False
line3 = False
line4 = False
line5 = False

for char in s:
    if char.isalnum():
        line1 = True
    if char.isalpha():
        line2 = True
    if char.isdigit():
        line3 = True
    if char.islower():
        line4 = True
    if char.isupper():
        line5 = True

print(line1)
print(line2)
print(line3)
print(line4)
print(line5)


#7-----Text Wrap-----
import textwrap

def wrap(string, max_width):
    result = []
    for i in range(0,len(string), max_width):
        result.append(string[i:i+max_width])
    return "\n".join(result)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
    
    
#8-----Designer Door Mat-----
n, m = map(int, input().split())

result = []
for x in range(1,n,2):
    result.append(('.|.'*x).center(m, '-'))
    
result.append("WELCOME".center(m, '-'))

for y in range(n-2,-1,-2):
    result.append(('.|.'*y).center(m, '-'))
    
for el in result:
    print(el)


#9-----String Formatting-----
def print_formatted(number):
    # your code goes here
    w = len(bin(number).replace('0b',''))
    l = []
    for i in range(1,number+1):
        l.append([str(i),oct(i).replace('0o',''),hex(i).replace('0x','').upper(),bin(i).replace('0b','')])
    for result in l:
        print(result[0].rjust(w), result[1].rjust(w), result[2].rjust(w), result[3].rjust(w))
        
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)FS


#10-----Alphabet Rangoli-----



#11-----Text Alignment-----
thickness = int(input()) #This must be an odd number
c = 'H'

#Top Cone
for i in range(thickness):
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

#Top Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

#Middle Belt
for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))    

#Bottom Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))    

#Bottom Cone
for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))


#12-----Capitalize!-----
def solve(s):
    l = []
    l+= s
    l[0] = l[0].upper()
    for i in range(1,len(l)):
        if l[i] == ' ' and l[i+1] != ' ':
            l[i+1] = l[i+1].upper()
            
    return ''.join(l)
               
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()


#13-----The Minion Game-----
def minion_game(string):
    # your code goes here
    pt_S = 0
    pt_K = 0
    
    for j in range(len(string)):
        if string[j] in ['A','E','I','O','U']:
            tot_substrings = len(string)-j
            pt_K+=tot_substrings

        else:
            tot_substrings = len(string)-j
            pt_S += tot_substrings
            
                
    if pt_S > pt_K:
        print('Stuart ' + str(pt_S) )
    elif pt_K > pt_S:
        print('Kevin ' + str(pt_K))
    else:
        print('Draw')

if __name__ == '__main__':
    s = input()
    minion_game(s)
    
    
#14-----Merge the Tools!-----
def merge_the_tools(string, k):
    # your code goes here
 
    for i in range(0,len(string),k):
        s = ''
        sub_sequence = string[i:i+k]
        for char in sub_sequence:
            if char not in s:
                s+= char
        print(s)

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)

#1-----Introduction to Sets-----
def average(array):
    # your code goes here
    arr_set = set(arr)
    return sum(arr_set)/len(arr_set)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
    
    
#2-----Symmetric Difference-----
M = int(input())
M_integers = set(map(int, input().split()))
N = int(input())
N_integers = set(map(int, input().split()))
    
union = M_integers.union(N_integers)
intersection = M_integers.intersection(N_integers)
symmetric_difference = union.difference(intersection)
    
for el in sorted(symmetric_difference):
    print(el)
    
    
#3-----Set .add()-----
n = int(input())
countries_set = set()
for _ in range(n):
    countries_set.add(input())

print(len(countries_set))


#4-----Set .discard(), .remove() & .pop()-----
n = int(input())
s = set(map(int, input().split()))

m = int(input())
for _ in range(m):
    comand = input().split()
    if comand[0] == 'pop' and len(s)>0:
        s.pop()
            
    elif comand[0] == 'discard':
        s.discard(int(comand[1]))
        
    elif comand[0] == 'remove':
        s.remove(int(comand[1]))
            
print(sum(s))


#5-----Set .union() Operation-----
n = int(input())
A = set(map(int, input().split()))
b = int(input())
B = set(map(int, input().split()))
    
result = A.union(B)
print(len(result))


#6-----Set .intersection() Operation-----
n = int(input())
A = set(map(int, input().split()))
b = int(input())
B = set(map(int, input().split()))
    
result = A.intersection(B)
print(len(result))


#7-----Set .difference() Operation-----
n = int(input())
A = set(map(int, input().split()))
b = int(input())
B = set(map(int, input().split()))
    
result = A.difference(B)
print(len(result))


#8-----Set .symmetric_difference() Operation-----
n = int(input())
A = set(map(int,input().split()))
m = int(input())
B = set(map(int,input().split()))

result = A.symmetric_difference(B)
print(len(result))


#9-----Set Mutations-----
n = int(input())
A = set(map(int,input().split()))
N = int(input())
for _ in range(N):
    operation,m = input().split()
    B = set(map(int,input().split()))
    
    if operation == 'intersection_update':
        A.intersection_update(B)
        
    elif operation == 'difference_update':
        A.difference_update(B)
        
    elif operation == 'update':
        A.update(B)
        
    else:
        A.symmetric_difference_update(B)
        
print(sum(A))


#10-----The Captain's Room-----
n = int(input())
rooms = list(map(int,input().split()))
set1 = set(rooms)

for i in set1:
    rooms.remove(i)

set2 = set(rooms)
result = list(set1.difference(set2))

print(result[0])

 
#11-----Check Subset-----
T = int(input())
for _ in range(T):
    n = int(input())
    A = set(map(int, input().split()))
    m = int(input())
    B = set(map(int, input().split()))
    print(A.issubset(B))


#12-----Check Strict Superset-----
A = set(map(int, input().split()))
n = int(input())

l_sets = []
for _ in range(n):
    l_sets.append(set(map(int,input().split())))

check_superset = False
for s in l_sets:
    check_superset = A.issuperset(s)

print(check_superset)


#13-----No Idea!-----
n, m = list(map(int, input().split()))
arr = list(map(int, input().split()))
A = set(map(int, input().split()))
B = set(map(int, input().split()))

tot = 0
for el in arr:
    if el in A:
        tot+=1
    
    if el in B:
        tot-=1
        
print(tot)


#1-----DefaultDict Tutorial-----


#2-----collections.Counter()-----
from collections import Counter

n = int(input())
shoe_sizes = list(map(int, input().split()))
counter = Counter(shoe_sizes)

customers = int(input())
customers_sizes = []
for _ in range(customers):
    s,p = map(int,input().split())
    customers_sizes.append((s,p))
    
result = 0
for k,v in counter.items():
    for s,p in customers_sizes:
        if k == s and counter[k]>0:
            result += p
            counter[k]-=1
            
print(result)
            

#3-----Collections.namedtuple()-----
from collections import namedtuple

n = int(input())
names = input().split()
register = namedtuple('register', names)
marks = []
for _ in range(n):
    col1, col2, col3, col4 = input().split()
    student = register(col1,col2,col3,col4)
    marks.append(student.MARKS)

marks = list(map(int,marks))
print(sum(marks)/len(marks))


#4-----Collections.OrderedDict()-----
from collections import OrderedDict

n = int(input())
d = OrderedDict()
for _ in range(n):
    l = input().split()
    k = ' '.join(l[:-1])
    if k in d:
        d[k] += int(l[-1])
    else:
        d[k] = int(l[-1])

for k,v in d.items():
    print(k,v)

    
#5-----Word Order-----
dic = {}
n = int(input())
for _ in range(n):
    word = input()
    if word in dic:
        dic[word]+=1
    
    else:
        dic[word] = 1
 
result = map(str, list(dic.values()))
print(len(dic.keys()))
print(' '.join(result))


#6-----Collections.deque()-----
from collections import deque

d = deque()
n = int(input())
for _ in range(n):
    l = input().split()
    if l[0] == 'append':
        d.append(int(l[1]))
        
    elif l[0] == 'appendleft':
        d.appendleft(int(l[1]))
        
    elif l[0] == 'pop' and len(d)>0:
        d.pop()
        
    elif l[0] == 'popleft' and len(d)>0:
        d.popleft()
        
s = ''
for el in d:
    s+=str(el)
    s+= ' '
    
print(s)


#7-----Company Logo-----
import math
import os
import random
import re
import sys

if __name__ == '__main__':
    s = input()
    dic = {}
    for char in s:
        if char in dic:
            dic[char] += 1
            
        else:
            dic[char] = 1

most_common = sorted(dic.items(), key=lambda x: x[0])
most_common = sorted(most_common, key=lambda x:x[1], reverse = True)[:3]

for char,n in most_common:
    print(char,n)
    
    
#8-----Piling Up!-----


#1-----Time Delta-----


#2-----Calendar Module-----
from calendar import weekday
import calendar

month, day, year = (int(x) for x in input().split()) 
number = weekday(year, month, day)
print(calendar.day_name[number].upper())


#1-----Exceptions-----
n = int(input())
for _ in range(n):
    a,b = input().split()
    try:
       r = int(a)/int(b)
       print(int(r))
        
    except ZeroDivisionError as e:
        print("Error Code: integer division or modulo by zero")
        
    except ValueError as e:
        if a.isnumeric():
            print ("Error Code: invalid literal for int() with base 10: '" + b + "'")
        else:
            print ("Error Code: invalid literal for int() with base 10: '" + a + "'")
 
   
#1-----Zipped!-----
n,x = map(int, input().split())
l = []
for _ in range(x):
    l.append(list(map(float, input().split())))
    
result = list(zip(*l))

for tup in result:
    average = sum(tup)/x
    print(average)
    
    
#2-----Athlete Sort-----
import math
import os
import random
import re
import sys



if __name__ == '__main__':
    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    k = int(input())
    
    sorted_column = sorted(arr, key = lambda x:x[k])
    
    for l in sorted_column:
        l = list(map(str,l))
        print(' '.join(l))


#3-----ginortS-----
s = input()
lowers = ''
uppers = ''
digits = ''
for char in s:
    if char.isalpha():
        if char.islower():
            lowers+=char
        
        else:
            uppers+=char
            
    else:
        digits += char
        
odds = ''
evens= ''

for num in digits:
    if int(num)%2 == 1:
        odds+=num
    else:
        evens+=num

result = ''.join(sorted(lowers)) + ''.join(sorted(uppers)) + ''.join(sorted(odds)) + ''.join(sorted(evens))
print(result)


#1-----Map and Lambda Function-----
cube = lambda x: x**3 # complete the lambda function 

def fibonacci(n):
    # return a list of fibonacci numbers
    a,b = 0,1
    result = []
    for x in range(n):
        result.append(a)
        a,b = b,a+b

    return result

        
if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
    
    
#1-----Detect Floating Point Number-----
import re 

T = int(input())
for _ in range(T):
    i = input()
    if re.match(r'^[+-]?[0-9]*\.[0-9]+$', i):
        print('True')
    else:
        print('False')



#2-----Re.split()-----
regex_pattern = r"[,.]"	# Do not delete 'r'.

import re
print("\n".join(re.split(regex_pattern, input())))


#3-----Group(), Groups() & Groupdict()-----
import re

s = input()
m = re.search(r'([a-z0-9])\1+',s)
if m:
    print(m.group(1))
else:
    print('-1')


#4-----Re.findall() & Re.finditer()-----
import re

s = input()

substrings= re.findall(r'[aeiouAEIOU]{2,}[qwrtypsdfghjklzxcvbnmQWRTYPSDFGHJKLZXCVBNM]', s)

for sub in substrings:
    print(sub[:len(sub)-1])
    
if len(substrings)==0:
    print('-1')


#5-----Re.start() & Re.end()-----


#6-----Regex Substitution-----


#7-----Validating Roman Numerals-----


#8-----Validating phone numbers-----


#9-----Validating and Parsing Email Addresses-----


#10-----Hex Color Code-----


#11-----XML Parser - Part 1-----


#12-----XML Parser - Part 2-----


#13-----Detect HTML Tags, Attributes and Attribute Values-----


#14-----Validating UID-----


#15-----Validating Credit Card Numbers-----


#16-----Validating Postal Codes-----


#17-----Matrix Script-----


#1-----XML 1 - Find the Score-----
def get_attr_number(node):
    # your code goes here
    integer_score = 0
    for child in node.iter():
        integer_score += len(child.attrib)
        
    return integer_score


#2-----XML2 - Find the Maximum Depth-----


#1-----Standardize Mobile Number Using Decorators-----


#2-----Decorators 2 - Name Directory-----


#1-----Zeros and Ones-----
import numpy

shape = list(map(int,input().split()))

list_z = numpy.zeros(shape,int)
list_o = numpy.ones(shape, int)

print(list_z)
print(list_o)


#2-----Array Mathematics-----


#3-----Arrays-----
import numpy

def arrays(arr):
    # complete this function
    # use numpy.array
    result = numpy.array(arr, float)
    return result[::-1]

arr = input().strip().split(' ')
result = arrays(arr)
print(result)


#4-----Shape and Reshape-----
import numpy
A = list(map(int, input().split()))
my_array = numpy.array(A)
print(numpy.reshape(my_array,(3,3)))


#5-----Transpose and Flatten-----
import numpy

n,m = map(int,input().split())
l1 = []
l2 = []
for _ in range(m):
    x = input().split()
    l2.append(list(map(int,x)))
    for el in x:
        l1.append(int(el))

my_array1 = numpy.array(l1)
my_array2 = numpy.transpose(l2)
print(my_array2)
print(my_array1.flatten())


#6-----Concatenate-----
import numpy

n,m,p = list(map(int,input().split()))
arr1 = []
arr2 = []
for _ in range(n):
    x = list(map(int,input().split()))
    arr1.append(x)
    
for _ in range(m):
    y = list(map(int,input().split()))
    arr2.append(y)
    
print(numpy.concatenate((arr1,arr2), axis = 0))


#7-----Eye and Identity-----
import numpy
numpy.set_printoptions(legacy='1.13')

n,m = map(int, input().split())
print(numpy.eye(n,m))


#8-----Floor, Ceil and Rint-----
import numpy
numpy.set_printoptions(legacy = '1.13')

A = list(map(float, input().split()))
my_array = numpy.array(A)
print(numpy.floor(my_array))
print(numpy.ceil(my_array))
print(numpy.rint(my_array))


#9-----Sum and Prod-----
import numpy
n, m = map(int, input().split())
my_array = []
for _ in range(n):
    my_array.append(list(map(int, input().split())))
    
my_array_sum = numpy.sum(my_array, axis = 0)
print(numpy.prod(my_array_sum, axis = 0) )
    
    
#10-----Min and Max-----
import numpy
n,m = map(int, input().split())
matrix = []
for _ in range(n):
    matrix.append(list(map(int, input().split())))
    
my_array = numpy.array(matrix)
min = numpy.min(my_array, axis=1)
print(numpy.max(min))
    
    
#11-----Mean, Var, and Std-----
import numpy

n,m = map(int,input().split())
matrix =[]
for _ in range(n):
    matrix.append(list(map(int, input().split())))
    
my_array = numpy.array(matrix)
print(numpy.mean(my_array, axis = 1))
print(numpy.var(my_array, axis = 0))
print(round(numpy.std(my_array),11))


#12-----Dot and Cross-----
import numpy
n = int(input())
A = []
B = []
for _ in range(n):
    A.append(list(map(int, input().split())))
    
for _ in range(n):
    B.append(list(map(int, input().split())))

print(numpy.matmul(A,B))


#13-----Inner and Outer-----
import numpy

A = list(map(int, input().split()))
B = list(map(int, input().split()))

print(numpy.inner(A,B))
print(numpy.outer(A,B))


#14-----Polynomials-----
import numpy
P = list(map(float,input().split()))
x = int(input())

print(numpy.polyval(P,x))


#15-----Linear Algebra-----
import numpy
n = int(input())
matrix = []
for _ in range(n):
    matrix.append(list(map(float, input().split())))
    
det = numpy.linalg.det(matrix)
print(round(det,2))
    
    
