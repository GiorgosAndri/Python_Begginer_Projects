import random
top_variable = random.randint(1, 1000)
top = (top_variable+ 1) * 2
r = random.randint(0, top)
print(r)
score = 0
guess = int(input("Guess the number: "))
while guess != r:
    if guess > r:
        score = score + 1
        guess = int(input("You need to go below: "))
    elif guess < r:
        score += 1
        guess = int(input("You need to go up: "))

if score == 0:
    print("Lots of luck I see. Congratulations!")
elif score == 1:
    print("Congratulations! You found it only with one try!")
else: print("After lots of patience and ", score , " tries, you found it")