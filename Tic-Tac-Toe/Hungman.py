import random
from words import words

lives_visual_dict = {
        0: """
                ___________
               | /        | 
               |/        ( )
               |          |
               |         / \\
               |
           """,
        1: """
                ___________
               | /        | 
               |/        ( )
               |          |
               |         / 
               |
            """,
        2: """
                ___________
               | /        | 
               |/        ( )
               |          |
               |          
               |
            """,
        3: """
                ___________
               | /        | 
               |/        ( )
               |          
               |          
               |
            """,
        4: """
                ___________
               | /        | 
               |/        
               |          
               |          
               |
            """,
        5: """
                ___________
               | /        
               |/        
               |          
               |          
               |
            """,
        6: """
               |
               |
               |
               |
               |
            """,
        7: "",
    }
word = random.choice(words)

wrongs = 5
count = 0
letter = "-"
lista = []
lista2 = []
used = []
#print(word)
#print(len(word))
for i in word:
    lista.append("-")
    lista2.append(i)
final = "".join(lista)
print(final)

while count < len(word) and wrongs > 0:
    letter = input("letter: ")
    if letter in used:
        print("You have already used that")
        continue
    if letter.lower() in word.lower():
        print("Great")

        used.append(letter)
        for i in lista2:
            if i == letter:
                n = lista2.index(i)
                count += 1
                #print(count)
                #print(n)
                lista[n] = letter
                lista2[n] = "-"
                #print(lista)
        final = "".join(lista)
        print(final.upper())
    else:
        print("You lose")
        wrongs -= 1
        print(lives_visual_dict[wrongs])
        used.append(letter)
        print(final.upper())
    print("You have used the letters: ", "".join(used))

if count == len(word):
    print("You win")
elif wrongs == 0:

    print("You're dead")
    print("The word was ", word.upper())






















