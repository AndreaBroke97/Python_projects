password = "123abc"
attempts = 3

counter = 0

while(counter < attempts):
    counter += 1
    
    a = input("Insert the password: ")
    a = a.strip().lower()


    if(a == password):
        print("Login effectuated with success") 
        break
    else:
        if(counter != 3):
            print(f"wrong password, number of attempts left:{attempts - counter} ")
        else:
            print("number of attempts expired. SYSTEM BLOCKED FOR 30 MINUTES")
            break
        
        
