# coding=utf-8

import csv
import random
import string


vocabulary = []

with open("netflix_titles.csv", encoding="utf8") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        countries = row['country'].split(",")
        if 'Italy' in countries:
            vocabulary.append(row['title'])

#print(vocabulary)  


letters = []
attempts = 10
guessed = ""

# Set seed per rendere replicabile gli esperimenti che facciamo 

random.seed(a=0)
random_index = random.randrange(0, len(vocabulary))

word = vocabulary[random_index].lower()

# print(word)

def init_guessed(plaintext):
    w = ""
    for l in plaintext:
       if l. isspace() or l in string.punctuation:
           w += l
       else:
           w += "-"
        


    return w 

def check_letter(l, w):
    found = False
    for i in w:
        if l == i:
            found = True
            break


    return found

def find_occurrencies(l, w):
    occurrencies = []
    for i in range(0, len(w)):
        if l == w[i]:
            occurrencies.append(i)
 
 
    return occurrencies

def sub_letters(l, pos, g):
    letters_list = list(g)
    letters_list[pos] = l
    return "".join(letters_list)

   
guessed = init_guessed(word)  
#print(guessed) 


game = True

while game:
    print("Prova ad indovinare! \n Il film misterioso è: {0} ".format (guessed))

    print("Hai ancora {} tentativi".format(attempts))

    choice = input("Indovina qual è il film (0 per uscire)")

    if choice == "0":
        game = False
        print("Ti sei arreso!")
        print("Il film misterioso è: {}".format(word))

    elif choice == word:
        print("Bravissimo hai indovinato!")    
        game = False

    else:
        print("\n----ERRORE----")
        print("Lettere già estratte: {}".format(letters))
        choice = input("Estrai una lettera:")
        choice = choice.lower()
        if check_letter(choice,letters):
            print("Lettera già scelta")

        else:
            letters.append(choice)   
            if check_letter(choice, word):
                occ =(find_occurrencies(choice, word))
                for pos in occ:
                    guessed = sub_letters(choice, pos, guessed)
                    print(guessed)
                


            else:
                print("LETTERA NON PRESENTE! ERRORE") 
                attempts -= 1
                if attempts <= 0:
                    print("Hai esaurito i tentativo!")
                    print("Il film misterioso era {}".format(word))
                    game = False
 

 



        
        



















        







        





    

