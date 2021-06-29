# epic car quiz

score = 0

print("\n\nWelcome to the epic car quiz")

print("\nPlease asnswer each question in lower case Eg. a, b, c")

q1 = input("\nQuestion 1 - What is faster in a quarter mile drag race\na. Porche 911 GT3 RS\nb. Honda Acura NSX\nc. Lamborghini Countach\n")

if q1 == "a":
    score = score + 5
elif q1 == "b":
    score = score
elif q1 == "c":
    score = score
else:
    score = score

q2 = input("Question 2 - What did peugeot make before it made cars\na. Bicycles\nb. Pepper grinders\nc. Corsets\nd. Ammunition\ne. All of the above\n")

if q2 == "a":
    score = score
elif q2 == "b":
    score = score
elif q2 == "c":
    score = score
elif q2 == "d":
    score = score
elif q2 == "e":
    score = score + 5
else:
    score = score

q3 = input("Question 3 - What car holds the lap record for the Nurburgring\na. Ferrari Laferrari\nb. Bughatti Chiron\nc. Porche 919 Hybrid\nd. Mercedes W12 Formula 1 car\n")

if q3 == "a":
    score = score
if q3 == "b":
    score = score
if q3 == "c":
    score = score + 5
if q3 == "d":
    score = score
else:
    score = score

q4 = input("Question 4 - When was the first car made\na. 1873\nb. 1886\nc. 1904\nd. 1914\n")

if q4 == "a":
    score = score
if q4 == "b":
    score = score + 5
if q4 == "c":
    score = score
if q4 == "d":
    score = score
else:
    score = score

q5 = input("Question 5 - Which car has the fastest accelaration\na. BMW M5\nb.Audi RS5\nc. Mercedes c300 ")

if q5 == "a":
    score = score + 5
if q5 == "b":
    score = score
if q5 == "c":
    score = score
else:
    score = score

print (score)

