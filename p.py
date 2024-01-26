''' multiline 
      comments
      datatypes
      type conversion
      i/o operation'''
import constant


print("hello")     
num1=6  
num2=7            
print(num1,num2)
name='pramod'       #create a variable #single line comment
print(name)      

a,b,c=5,3.4,'hello world'    #create  multivalues to maltivariables
print(a,b,c)

print(constant.pi)             #importing pi and gravity
print(constant.gravity)

number1=5
print(number1,'is type of',type(number1))
number2=3.5
print(number2,'is type of',type(number2))         #to display datatypes,int,str,complex
number3=3+4j
print(number3,'is type of',type(number3))

languages=['python','c++','java']                #create a list
print(languages[0])
print(languages[2])
print(languages,'is of type',type(languages))

product=('tv','sony',45880.0)
print(product[0])                              #create a tuple
print(product,'is of type',type(product))

std_id={11,12,13,14}                               #create a set
print(std_id ,'is of type',type(std_id))

capital_city={'India':'Delhi','US':'Washington DC','china':'beijing'}           #create a dictionary
print(capital_city,'is of type',type(capital_city)) 



intnum=14
floatnum=15.5
sum=intnum+floatnum
print(sum,'is of type',type(sum))                                        #type conversion

num_str='12'
num_int=23
sum=int(num_str)+num_int
print(sum)                                    

  #ip/op operations

print('hi good morning', end='***')                       
print('how was the day')                                     #it ends with ***

print('hi hello',122223,'who are u',sep='!!!!!!!!!!!')          #it saperates by !!!!!!!!!!
print('u r beautiful'+' awesom')                                # + operator joins



a,b=2,3
print(a>b)                           #false
print(a<b)                           #true
print((a<b) and (b<5))
print((a>1)or (b>1))

a1,b1=2,2 
print('identity op')                            #identity oeprator 'is' ,'is not'
a2,b2='hi','hi'
print(a1 is not b1)                   #false
print(a2 is b2)

x='Heloo google'           #membership operator 'in','not in'
y={1:'a',2:'b',3:'c'}
print('membership op')
print('H' in x)               #true
print('hell' not in x)
print(1 in y)
print('a' in y)                 #false


'''flow control
      statements 
        if
        if else
        if elif 
        nested if
        for
        while'''

if 10>11 :                                               #if
    print('10 >11')

if 10>5 :                                                #if else
    print('10 is greater than 5')
else :
    print('5 is grater than 10') 


marks=45                                               #elif
if marks>=80 and marks<=100 :
    print('a grade')
elif marks>=50 and marks<80:
    print('b grade')
elif marks>=35 and marks<50 : 
    print('pass')
elif marks>=0 and marks<35:
    print('fail')
else :
    print('invalid marks')


rank=8                                            #nested if
if rank<30:
    print(' 10 points',end='+')
    if rank<20:
        print('5 points',end='+')
        if rank<10:
            print('3 points')
            
print('for loop...........')                     #for loop            
x='python'
for x in  'python':
  print(x)

val=range(5)
for i in val:
    print(i)

for i in range(1,4,1):
    print('manoj',i)

for val in languages:         #val is str
    print(val)


i,n=1,5                                              #while
while i<=5:
 print('while executeing',i) 
 i+=1

num=0                                                #continue
while num<10:
  num+=1
  if(num%2==0):                  
   continue        #if it even continue from while
  print(num)       #ptint odd

if num==0:                                            #pass
   pass            #write a  if code or pass 

"""python
 functions"""


 