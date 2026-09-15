import os
os.system("cls")
#EXERCISE 1: squares
'''
squares = [i ** 2 for i in range(10)]
print(squares)
'''

#######################################################

#EXERCISE 2: Uppercase
'''
names = ["alice", "bob", "charlie"]

names = [a.upper() for a in names]
print(names)
'''

#######################################################

#EXERCISE 3: Long
'''
words = ["python", "code", "list", "comprehension"]

lw = [len(word) for word in words]

print(lw)
'''

#######################################################

#EXERCISE 4: number even
'''
num = [i for i in range(21) if i % 2 == 0]
print(num)
'''

#######################################################

#EXERCISE 5: string filter
'''
fruits = ["pear", "strawberry", "peach", "lemon", "apple"]

new_list = []

for fruit in fruits:
    
    if "p" in fruit:
        new_list.append(fruit.upper())
        

print(new_list)
'''

#######################################################

#EXERCISE 6: even/odd
'''
l1 = []

for i in range(0, 10):

    value_type = f" {i} Even" if i % 2 == 0 else f" {i} Odd"

    l1.append(value_type)
    
print(l1)   
'''
 
#######################################################
 
#EXERCISE 7: positive/negative
'''
numbers = [-3, -1, 0, 2, 5]

num = []

for el in numbers:
    
    other_list = f"{el} = Positive" if number > 0 else f"{el} = Negative"
    
    num.append(other_list)
    
print(num)
'''

#######################################################

#EXERCISE 8: Dictionary
'''
student = {
    
    "name": "andrea".capitalize(),
    "age":   19,
    "grade": "junior".capitalize()
}

print(student["age"])
'''

#######################################################

#EXERCISE 9: secure access
'''
car = {
    "brand": 
    "Toyota", 
    "year": 2020
    }

print(car.get("price")) #none
'''

#######################################################

#EXERCISE 10: update
'''
car = {
    "brand": "Toyota", 
    "year": 2020
    }

car.update({
    "price": 15000,
    "year": 2018
})

print(car)
'''

#######################################################

#EXERCISE 11: complete iteraction
'''
product = {
    "year": 2020,
    "item": "1542-22130086",
    "society": "PRGR S.R.L"
}



for x in product:
    x = product.items()
    print(x)
'''

#######################################################

#EXERCISE 12: sum
'''
num1 = float(input("Insert the most number: "))
num2 = float(input("Insert the second number: "))

def numbers(num1, num2):
    result = num1 + num2

    return result

print(numbers(num1, num2))
'''

#######################################################

#EXERCISE 13: valutation
'''
num1 = int(input("Enter the most number: "))


def vote(num1):
    if num1 > 15:
        return "Pass"
    else:
        return "Fail"

print(vote(num1))
'''
    
#######################################################ù

#EXERCISE 14: Student
'''
def student(name, age, grade):
    print(f"Name: {name}, Age: {age}, Grade: {grade}") #arguments
    
    
student("Andrea", 19, "Junior") #positional arguments = sono passati in ordine in base alla funzione senza specificare cosa e "Andrea" etc
student(name = "Andrea", grade = "Junior", age = 20) #keyword arguments = specifichi il nome del parametro seguito dal valore.
'''

#######################################################

#EXERCISE 15: default
'''
def order(drink = "water"):
    print(f"i drink {drink}")
    
order() #usa il default
'''

#######################################################

#EXERCISE 16: variable sum

'''
def summing(*args):
    result = 0
    for n in args:
        result += n
    return result

n1 = float(input("Enter numbers: "))
n2 = float(input("Enter numbers: "))
n3 = float(input("Enter numbers: "))

print(summing(n1, n2, n3))
'''

#######################################################

#EXERCISE 17: profile
'''
def people(**kwargs):
    
    for key, value in kwargs.items():  
#con **kwargs raccogliamo tutti gli argomenti che arrivano senza limite e raccogliamo le chiavi
#con .items() abbiamo accesso a chiavi e valori
        
        print(f"{key}: {value}")
    
people(name = "Andrea", age = 20)

people(name = "Vittoria", age = 25, city = "Milano", job = "Developer")
'''

#######################################################

#EXERCISE 18: local scope
'''
name = "Andrea"

def saluta():
    name = "Alice"   # locale, non tocca quella fuori
    print(name)      # → "Alice"

saluta()
print(name)          
'''

#######################################################
'''
#EXERCISE 19: global
name = "Andrea"

def saluta():
    global name
    name = "Alice"   # modifica quella globale

saluta()
print(name)          
'''

#######################################################

#EXERCISE 20: Ricursion
'''
def factorial(n):
    if n == 0 or n == 1:
        return 1 #valore che si restituisce quando si arriva al caso base
    return n * factorial(n - 1)

print(factorial(4))  # → 24
print(factorial(5))  # → 120
'''

#######################################################

#EXERCISE 21: recursive sum
'''
def sum(n):
    if n == 0:
        return 0
    return n + sum(n - 1)
    
print(sum(0))
print(sum(10))
'''

#######################################################ù

#EXERCISE 22: double
'''
numbers = [1, 2 ,3 ,4, 5]

result = list(map(lambda x: x * 2, numbers))
#map() prende una funzione e una lista, e applica la funzione a ogni elemento.
#lambda x: x * 2 — prende x, restituisce x * 2. quindi raddioppia il un numero x con 2
print(result)
'''

#######################################################

#EXERCISE 23: Filter
'''

numbers = [1, 2 ,3 ,4, 5, 10, 20, 40, 2, 0]

result = list(filter(lambda x: x > 10, numbers))

print(result)
'''

#######################################################

#EXERCISE 24: base class
'''
class Person:
    
    def __init__ (self, name, age):
        self.name = name
        self.age = age
        
    def greet(self):
        print("ciaooo")
        
p1 = Person("Andrea", 20)
p1.greet()
'''

#######################################################

#EXERCISE 25: mutiple objects
'''
class Person:
    
    def __init__(self, name, age): 
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello! My name is {self.name} and I am {self.age} years old")
    
p1 = Person("Andrea", 19)
p2 = Person("Luca", 29)

p1.greet()

p2.greet()
'''

#######################################################

#EXERCISE 26: metods with parameters
'''
class Person:
    def __init__(self, name):
        self.name = name
        #self.age = age
        
   
        
    def travel(self, from_place, to_place):
        print(f"{self.name} is travelling from {from_place} to {to_place}\n")
        
   
p1 = Person("Andrea")
p1.travel("Rome", "Milan")
'''

#######################################################

#EXERCISE 27: metod with return
'''
class Person:
    def __init__(self, name):
        self.name = name
        #self.age = age
        
   
        
    def travel(self, from_place, to_place):
        self.from_place = from_place
        self.to_place = to_place
        print(f"{self.name} is travelling from {from_place} to {to_place}\n")
        
    def __str__(self):
        return f"DESCRIPTION: \nName: {self.name}, \nStart: {self.from_place}, \nDestination: {self.to_place}"
   
p1 = Person("Andrea")
p1.travel("Rome", "Milan")

print(p1)
'''

#######################################################

#EXERCISE 28: grade analysis
'''
voteList = [12, 17, 22, 68, 28, 90, 32]

elist = [vote for vote in voteList if vote >= 60]

def avg(vote):
    return sum(vote) / len(vote) #len conta gli elementi e divide la somma per il numero di voti e ottiene la media
    

print(voteList)
print(elist)
print(avg(elist))
'''

#######################################################

#EXERCISE 29: votes analysis
'''
class Student:
    def __init__(self, name, surname, vote):
        self.name = name
        self.surname = surname
        self.vote = vote
        
        
    def __str__(self):
        
        return (f"Name: {self.name}, \nSurname: {self.surname}, \nVote: {self.vote}\n")
        
        
p1 = Student("Andrea", "Di natale", 14)
p2 = Student("Luca", "Acquaviva", 28)
p3 = Student("Filippo", "Barresi", 10)
p4 = Student("Salvatore", "Germano", 30)
p5 = Student("Paolo", "Lenzo", 15)

Students = [p1, p2, p3, p4, p5]
Students.append(p1)

for People in Students:
    if People.vote > 25:
        print(People)
''' 

#######################################################
'''
#EXERCISE 30: functional pipeline
#parta da una lista di numeri
#● usi filter, map, lambda
#● produca una nuova lista di quadrati solo dei numeri pari

elist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#lambda e una funzione anonima, si usa per semplici operazioni in una riga
#filter scorre la lista tenendo solo gli elementi che rispettano la condizione usando condizioni
#map scorre la lista e trasforma ogni elemento usando operazioni
#list converte il risultato di filter/map in una lista vera
newlist = list(map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, elist)))
#newlist = list(map(lambda x: x ** 2, newlist))

print(newlist)
'''