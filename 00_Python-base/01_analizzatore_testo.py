#ANALIZZATORE DI TESTO

word = input("\nenter a word: ")

vocal = 0
consonant = 0
uppercase = 0
space = 0
specialChar = 0

words = word.split() #spezza la stringa in una lista di parole
num_words = len(words)#conta quanti elementi ha la lista

for letters in word:
    if letters in "aeiou":
        vocal +=1
    elif letters.isupper():
#is upper controlla se un char o string e maiuscolo
        uppercase +=1
    elif letters.isalpha() and letters not in "aeiou": 
#isalpha() controlla se il carattere e una lettera dell'falfabeto
        consonant += 1
    elif letters.isspace():
#is space controlla se un carattere e uno spazio
        space += 1
    elif not letters.isalnum() and not letters.isspace():
#is alnum controlla se un carattere e una lettera o numero
        specialChar += 1
        
print(f"\nword separated by space: {words} ")
print(f"word lenght separated by space: {num_words} ")
print(f"vocal present: {vocal} ")
print(f"consonant present: {consonant} ")
print(f"uppercase present: {uppercase} ")
print(f"space present: {space} ")
print(f"special character present: {specialChar} \n")

####

riddle = input("\nenter the correct word: ")
valid = 3
secret = "apple"

while not riddle.isalpha():
    valid -= 1
    if valid > 0:
        riddle = input("try again: ")
    else:
        print("\nERROR.. quitting.")
        break
    
asterisks = "*" * len(secret)
print(f"the word to guess is {asterisks}")


#list
guessed = []
attempts = 5
while attempts > 0:
    guess = input("enter the lecter presented in the word: ")
    guessed.append(guess)
    print(f"the letters searched so far are: {guessed}")
    attempts -= 1
    
        
if riddle.strip().lower() == secret:
    print("correct you guessed the word!")
else:
    print("wrong!")
