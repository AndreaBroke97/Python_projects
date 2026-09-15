#EXERCISE 1: major, minor or equal
'''
a = input("Insert a number: ")
b = input("Insert another number: ")

if(a > b):
    print(f"{a} is greater than {b}")
elif(a < b):
    print(f"{a} is lower than {b}")
else:
    print(f"{a} is equal of {b}")
'''

#<---------------------------------------------------->

#EXERCISE 2: verify, if are equal, true, (o) ,false
''' 
x = int(input("insert one number: "))
y = float(input("insert the second number: "))

print(x == y)
print(type(x), type(y))
'''

#<---------------------------------------------------->

#EXERCISE 3: lexic graphic compare
'''
a = input("insert a sentence: ")
b = input("insert another sentence: ")

if(a < b):
    print(f"{a} is lower then {b}")
elif(a > b):
    print(f"{a} is greater then {b}")
else:
    print(f"{a} and {b} are equal")
'''

#<---------------------------------------------------->

#EXERCISE 4: Case Insensitive
'''
a = input("insert a sentence: ")
b = input("insert another sentence: ")

if(a.lower() == b.lower()):
    print(f"{a} is equal to {b}")
elif(a.lower() != b.lower()):
    print(f"{a} is different to {b}")
else:
    print("ERROR")
'''
    
#<---------------------------------------------------->

#EXERCISE 5: Access control
'''
age = int(input("insert age: "))

if (age >= 18):
    has_id =  ("Access granted")
else:
    has_id =  ("Access denied")
    
print(has_id)
'''

#<---------------------------------------------------->

#EXERCISE 6: Age
'''
while True:
    age = int(input("insert age: (or 0 to exit): "))

    if age == 0:
        break

    if (age <= 13):
        print("child")
    elif (age > 14 and age < 17):
        print("teen")
    else:
        print("adult")
'''

#<---------------------------------------------------->

#EXERCISE: While
'''
while True:
    a = int(input("insert the first number: "))
    b = int(input("insert the second number: "))
    c = int(input("insert the third number: "))



    if a > b and a > c:
        print("you are strong")
    else:
        print(f"{a} is not the greatest.")
        
        choose = input("you want to exit? (y/n): ")
        if choose == "y":
            break
'''

#<---------------------------------------------------->

#EXERCISE: Count
'''
a = 1

while a <= 10:
    print(a)
    a += 1 #incremento di 1
'''

#<---------------------------------------------------->

'''
a = int(input("insert the first number: "))
b = int(input("insert the second number: "))

result = 0
i = 0

while i < b:
    result += a
    i += 1
    
    print(f"the product of {a} and {b} is {result}")
'''

#<---------------------------------------------------->

#EXERCISE 7: compost expression
'''
while True:
    username = input("insert the username: ")
    password = input ("insert the password: ")
    if username == "admin" and password == "123":
        print("login Ok")
        
        choice = input("You want to exit? (y/n): ")
        if choice == "y":
            break
    else:
        print("Login failed")
    
        choice = input("You want to exit? (y/n): ")
        if choice == "y":
            break
'''

#<---------------------------------------------------->

#EXERCISE 7:  compost expression with ( ) not, or
'''
while True:
    username = input("insert the username: ")
    password = input ("insert the password: ")
    if not (username == "admin" or password == "123"):
        print("login Ok")
        
        choice = input("You want to exit? (y/n): ")
        if (choice == "y"):
            break
    else:
        print("Login failed")
    
        choice = input("You want to exit? (y/n): ")
        if (choice == "y"):
            break
'''   

#<---------------------------------------------------->

#EXERCISE 7 : compost expression with ( ), or, not
'''    
while True:
    username = input("insert the username: ")
    password = input ("insert the password: ")
    if not(username == "admin" and password == "123"):
        print("login Ok")
        
        choice = input("You want to exit? (y/n): ")
        if (choice == "y"):
            break
        
    else:
        print("Login failed")
    
        choice = input("You want to exit? (y/n): ")
        if (choice == "y"):
            break
'''     

#<---------------------------------------------------->

#EXERCISE 9 : compost expression with ( ), or
'''        
while True:
    username = input("insert the username: ")
    password = input ("insert the password: ")
    if(username == "admin" or password == "123"):
        print("login Ok")
        
        choice = input("You want to exit? (y/n): ")
        if (choice == "y"):
            break
        
    else:
        print("Login failed")
    
        choice = input("You want to exit? (y/n): ")
        if (choice == "y"):
            break
'''

#<---------------------------------------------------->

#EXERCISE 9: vote valutation
'''
while True:
    vote = int(input("insert number between (0-100): "))
    
    if vote < 60:
        print("Fail\n")
    elif vote > 60 and vote < 79:
        print("Pass\n")
    elif vote >= 80:
        print("Excellent!")

    choice = input("For exit insert (0), for continue insert (1): ")
    if (choice == "0"):
        break
    
    elif (choice != "1"):
        print("Invalid input, please insert 0 or 1")
        continue
'''

#<---------------------------------------------------->

#EXERCISE 10: user input
'''
while True:
    a = int(input("insert a number negative or positive: "))

    if a > 0:
        print("Positive")
    elif a < 0:
        print("Negative")
    
    choice = input("You want exit? (y/n): ")
    if choice == "y":
        print("Program finished")
'''

#<---------------------------------------------------->

#EXERCISE 11: even or odd
'''
while True:
    n = int(input("insert a number: "))

    if n % 2 == 0:
        print("Even")
    else:
        print("Odd")
    
    choice = input("You want exit? (y/n): ")
    if choice == "y":
        print("Program finished")
'''

#<---------------------------------------------------->

#EXERCISE 12: user state
'''
while True:
    answer = input("Are you logged in? (yes/no): ")
    if answer == "yes" or answer == "no":
        break
    print("Invalid input, please insert yes or no")

logged_in = answer == "yes"
status = "Active" if logged_in else "Inactive"
print(status)
'''

#<---------------------------------------------------->

#EXERCISE 13: menu
'''
print("//-----MENU-----//")
print("HELLO 😊 FOR INFO INSERT (help) ")

active = False

while True:
    command = input("insert a command: ").lower().strip() #lower accetta ciò che l'utente scrive in maiuscolo || lo strip rimuove eventuali spazi al'inizio o alla fine
    
    match command:
        case "help":
            print("\nTHE COMMAND DISPONIBLE IS:")
            print("(start) for starting the system.\n")
            print("(stop) for stopping the system.\n")
            print("(restart) for reload the system.\n")
            print("(status) for status of the system.\n")
            print("(exit) for quit the system.\n")
        case "start":
            if active:
                print("The system is on")
            else:
                active = True
                print("Starting")
        case "stop":
            if not active:
                print("The system is of")
            else:
                active = False
                print("Arresting")
        case "restart":
            print("reloading")
            active = False
            active = True
            print("System is reloaded")
        case "status":
            if active:
                print("Status: ACTIVE ✅")
            else: 
                print("Status: DISACTIVED ⛔")
        case "exit":
            print("quitting")
            break
        case _:
            print("Unknown command")
'''

#<---------------------------------------------------->

#EXERCIZE 14: days of the week
'''
print("\nHELLO! if you want quit, enter (exit). or for continue")
while True:
    week = input("enter a Day of the week: ")
    
    match week:
        case "monday":
            print("\nWeek day.")
        case "tuesday":
            print("Week day.\n")
        case "wednesday":
            print("Week day.\n")
        case "friday":
            print("Week end.\n")
        case "saturday":
            print("Week end.\n")
        case "sunday":
            print("Week end.\n")
        case "exit":
            print("Au revoir")
            break
        case _:
            print("\nUnknown command, please repeat.\n")
'''      
        
#<---------------------------------------------------->

#EXERCISE 15: contator
'''     
num = 1

while (num <= 10):
    print(f"{num}")
    num += 1
'''     
#<---------------------------------------------------->

#EXERCISE 16: password loop
'''   
password = input("\ninsert the password: ")

while password != "python":
    print("Error, please try again")
    password = input("\ninsert the password: ")
    
    print("\nAccess granted")
'''   

#<---------------------------------------------------->

#EXERCISE 17: tentative counting
'''   
numbers = [] #array vuoto
contator = 0
num = int(input("Insert a number (0 for quit): "))
numbers.append(num) #append aggiunge un elemento a quelli già salvati nella  lista [1,2,3 (7 aggiunta)]

while num != 0:
    num = int(input("Insert a number (0 for quit): "))
    numbers.append(num)

for num in numbers: #per ogni numero salvato nella lista ne prendo uno alla volta
    if num > 0: #se è positivo 
        contator += 1 #aumenta di 1
        
print(f"Numbers positive inserted: {contator}")
'''   
 
#<---------------------------------------------------->

#EXERCISE 18: search flag
'''   
print("\nhi 😊 if you want quit insert (stop) or")
running = True #finchè running è True, vai avanti

while running: #finchè running e True continua
    text = input("\nInsert a string: ")
    
    if text == "stop":
        running = False
    else:
        print(f"You have insert: {text}")
'''   

#<---------------------------------------------------->

#EXERCISE 19: skip multiples
'''   
num = 20
for  i in range (1, 21):
    if i % 3 == 0:
        continue
    print(i)
'''   

#<---------------------------------------------------->

#EXERCISE 20: controlled interruption numbers divisible by 7
'''   
num = int(input("\nInsert numbers: "))

while True: #esegue tutto fino al break
    print(num) #stampa i numeri correnti tramite il contatore
    if num % 7 == 0: #controlla se il numero è divisibile per 7, se True si ferma.
        print(f"\nThe numbers divisibile by 7 is: {num}")
        break
    num += 1 #contatore
'''   

#<---------------------------------------------------->

#EXERCISE 21: sum
'''   

total = 0

for i in range(1, 101):
    total += i #ad ogni giro aggiunge il numero corrente al totale
    
print(f"The total of sum is: {total}")
'''   

#<---------------------------------------------------->

#EXERCISE 22: print all even numbers from 2 to 50, personalized step
'''   
for i in range(2, 51):
    if i % 2 == 0:
        print(i)
'''   

#<---------------------------------------------------->

#EXERCISE 23: list of names

'''
name = input("\nEnter a name, for quit enter (stop):  ")
names = [].append(name)

for names in name:
    print(name)
    break
'''   

#<---------------------------------------------------->

#EXERCISE 24: enumerate, list of products
'''   
products = []
prod = input("\nInsert a product for quit enter (stop): ")

while prod != "stop": #raccoglie tutti i prodotti con il while
    products.append(prod) #aggiunge il prodotto alla lista
    prod = input("\nInsert a product for quit enter (stop): ")
    
for i, product in enumerate(products): #enumerate aggiunge automaticamente un numero davanti ad ogni elemento 1-, 2-, 3-
    #per ogni coppia (indice, valore) nella lista enumerate(products)
    print(f"{i} - {product}")
'''   
#<---------------------------------------------------->

#EXERCISE 25: number filter
''' 
numbers = [15, -3, 75, 2, 5, 0, 10, 20]

for num in numbers:

    if num == 0:
        break
    if num < 0:
        continue
    if num > 10:
        print (num)
''' 
    
#<---------------------------------------------------->

#EXERCISE 26: mini validator, username and password
'''
print("if you want quit, enter (exit)")
username = input("enter username: ")
password = input("enter a 6 - char long password: ")

exited = False
while username == "" or len(password) < 6:
    
    if username == "exit":
        exited = True
        print("program finished")
        break
    
    print("invalid, try again")
    username = input("enter username: ")
    password = input("enter a 6 - char long password: ")
     
if exited:
    print("program finished")
else:
    print("valid")
'''

#<---------------------------------------------------->

