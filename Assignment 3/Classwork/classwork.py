x= list (range(0,10))
y=[]
for each in x:
        y.append(each**2)
print(y)
................................................


Fast Method

z=[each**2 for each in range(0,10)]
print(z)

.................................................
x= list (range(0,10))
y=[]
for each in x:
if each % 2=0:
        y.append(each**2)
print(y)
.................................................

programming_lang= ["c", "Python", "java"]
creator= ["Dennis", "Ram", "James"]

d={}
for each in zip(programming_lang, creator):
  d[each(0)]=each[1]
prind(d)  


or

d={}
for key, val in zip(programming_lang, creator):
  d[key]= val
print(d)  


.................................................


def sum(a,b):
    return a+b

print(sum(1,2))

.................................................

def sum(a,b):
    return a+b

a= lambda a,b: a+b           (implicitely return)
print(a(5,6))

..................................................
def sum(a,b):
    return a+b
    return a-b

print(sum(1,2))    

Error

def sum(a,b):
    yield a+b
    yield a-b

print(sum(1,2))    

Wrong

def sum(a,b):
    yield a+b
    yield a-b

print(next(sum(1,2)))    

Right but only prints first output


def sum(a,b):
    yield a+b
    yield a-b


gen_sum= sum(1,2)
print(next(gen_sum))
print(next(gen_sum))
                       print(next(gen_sum)) #StopIteration xx
CORRECT
  
.....................................................................


def sum(a,b):
    yield a+b
    yield a-b


gen_sum= sum(1,2)

for each in gen_sum: 
    print(each)

.....................................................................

def sum():
    i=0
    yield i
    i+=1
    yield i
    i+=100
    yield i


gen_sum= sum()

for each in gen_sum: 
    print(each)

.....................................................................

l= [x for x in range(1,10000)]
g= (x for x in range(1,10000))

print("Memory consumed by list l: ", l.__sizeof__())
print("Memory consumed by generator g: ", g.__sizeof__())
    
.....................................................................

def sum(a,b):
    return a+b

a= sum
print(type(a))

      
def accept func(a):
      print(a(1,2))

accept func(a)      


def outer():
	def inner(a,b):
        	return a+b

x=outer()
print(x.__name__)
	
........................................................................

def outer(arg_func): 
    def inner():     
        print("Inner executed")
        arg_func()  
    return inner 

@outer
def my_func():
    print("Hello World!")

my func()

........................................................................


class Car:
    pass

tesla = Car()
print(type(tesla))


class Car:

    def __init__(self, wheels,engine):
        self.wheels= wheels
        self.engine= engine

kia = Car(4, "diesel")
print(kia)


.......................................................................

class Car:

    def __init__(self, name, wheels,engine):
        self.name= name
        self.wheels= wheels
        self.engine= engine

    def drift(self):
        print(f" {self.name} is drifting")
        


kia = Car("kia" ,4, "diesel")
tesla = Car( "tesla" ,6, "electric")

kia.drift()
tesla.drift()

print(isinstance(kia, Car))
print(isinstance(kia, object))
print(isinstance(kia, int))

..........................................................................
class Animal:
    def __init__(self,type):

class Dog(Animal):
    def __init__(self, name, type):
        super().__init__(self)
        self.name=name
        self.type=type

d= Dog("tom", "carni")
print(d.__dict__)
print(isinstance(d, Animal))
print(isinstance(d, type))
print(isinstance(d, carni))

...........................................................................

class Person:

    count= 0

    def__init__(self, fname, lname):
        self.fname=fname
        self.lname=lname
        person.count+=1

        def get_email(self):
            return f"{self.fname}.{self.lname}@deerwalk.edu.np"

        @property
        def full_name(self):
            return f"{self.fname} {self.lname}"

        @classmethod
        def generate_person_instance(cls, dashed_name):
            fname, -lname= dashed_name.split("-")
            return cls(fname, lname)

p= Person.generate_person_instance("Hari-Bahadur")
print(p.__dict__)

.........................................................................

class TempConverter:

    @staticmethod
    def cel_to_far(ctemp):
        return ctemp*(9/5)+32


    @staticmethod
    def far_to_cel(ftemp):
        return (5/9)*(ftemp-32)

print(TempConverter.cel_to_far(100))
print(TempConverter.far_to_cel(212))

..........................................................................
                
        
        






