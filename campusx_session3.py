# ********* nested loop *******
'''for i in range(1,5):
  for j in range(1,5):
    print(i,j)


rows = int(input('enter number of rows'))

for i in range(1,rows+1):
  for j in range(1,i+1):
    print('*',end='')
  print() 


#**************** Loop Control Statement*************#
# Break

for i in range(1,10):
  if i == 5:
    break
  print(i)

# Continue
for i in range(1,10):
  if i == 5:
    continue
  print(i)

# Pass
for i in range(1,10):
  pass

#**********String***************
# Strings are sequence of Characters

# In Python specifically, strings are a sequence of Unicode Characters

# Creating Strings
# Accessing Strings
# Adding Chars to Strings  ---> not possible
# Editing Strings     ---> not possible
# Deleting Strings    ---> not possible (you can delete whole string with use of del function)
# Operations on Strings
# String Functions 

#Creating Stings
s = 'hello'
s = "hello"
# multiline strings
s = ''hello''
s = """hello"""
s = str('hello')
print(s) 

#Accessing Strings
# Positive Indexing
s = 'hello world'
print(s[4])

# Negative Indexing
s = 'hello world'
print(s[-3])

# Slicing
s = 'hello world'
print(s[6:0:-2])

print(s[::-1])    #output---> dlrow olleh

s = 'hello world'
print(s[-1:-6:-1])   #Always remember the position of (-1) is always greater than the position of (-6)
# the position of (-1) is d

# Editing and Deleting in Strings

# s = 'hello world'
# s[0] = 'H'

# Python strings are immutable ---> immutable means not changeable (you cannot edit and delete a word in string)
# But you can Delete whole string 

# del s
# print(s) 

#*************Operation on strings**********
# Arithmetic Operations
print('delhi' + ' ' + 'mumbai')

print('delhi'*5)

# Relational Operations

print('delhi' != 'delhi')

print('mumbai' > 'pune')  # lexiographically

print('Pune' == 'Pune')

# Logical Operations

print('hello' and 'world')

print('hello' or 'world')

print('' and 'world')

print('' or 'world')

print(not 'hello')

# Loops on Strings
for i in 'hello':
  print(i)

# Membership operators

print('D' in 'delhi')

#********** Len Function***********

print(len('hello world'))
s = 'rajnish'
print(len(s))

#********** Max Function *******

print(max('hello world'))

#********** Min Function *******

print(min('hello world'))

#************ Sorted Function *********

print(sorted('hello world'))

print(sorted('hello world',reverse=True))

#*********** Capitalize Function**********
s = 'hello world'
print(s.capitalize())
print(s)

#*********** Title Function**********
print(s.title())

#*********** Upper Function**********
print(s.upper())

#*********** Lower Function**********
print(s.lower())

#***********Swapcase Function*********
s1 = 'raJniSH'
print(s1.swapcase())

#***********Count/Find/Index********
print('my name is rajnish'.count('i'))

print('my name is rajnish'.find('x'))  # --->they throw -1 if word is not present

# print('my name is rajnish'.index('x'))  # --->they throw error if word is not present

# ****************endswith/startswith**********
s1 = 'my name is rajnish'

print(s1.startswith('my'))

print(s1.endswith('sh'))

#************ Format Function ************
name = 'Rajnish'
gender = 'male'

print('Hi my name is {1} and I am a {0}'.format(gender,name))

# ************isalnum/ isalpha/ isdigit/ isidentifier******

print('nitish1234%'.isalnum())  #---> if all digit are alphabet or all number not any identifier here % is identifier

print('nitish'.isalpha())

print('123abc'.isdigit())

print('first-name'.isidentifier())'''

#************** Split and Join Function *********

s1 = "my name is rajnish patel"
print(s1.split())

s2 = ' '
s3 = ['hi', 'my', 'name', 'is', 'nitish']

print(s2.join(s3))

#***************Replace Function*******
print('hi my name is nitish'.replace('nitish','campusx'))

#************strip***********

print('nitish        raj                   '.strip())

# Write a program that can check whether a given string is palindrome or not.
# abba
# malayalam

s = input('enter the string')
flag = True
for i in range(0,len(s)//2):
  if s[i] != s[len(s) - i -1]:
    flag = False
    print('Not a Palindrome')
    break

if flag:
  print('Palindrome')

