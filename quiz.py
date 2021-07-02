# epic car quiz

score = 0

print("\n\nWelcome to the epic car quiz")
print("\nPlease asnswer each question in lower case Eg. a, b, c")

# TODO make a function ask. Make it ask the question and only allow valid answers.
# TODO give feedback to user if they give an invalid answer
def ask(question, answers):
    response = None
    while response not in answers:
        response = input(question)
        if response not in answers:
            print ("\nPlease input an actual answer")
    return response


q1 = ask("\nQuestion 1 - What is faster in a quarter mile drag race\na. Porche 911 GT3 RS\nb. Honda Acura NSX\nc. Lamborghini Countach\n", ['a', 'b', 'c'])
if q1 == "a":
    score = score + 5


q2 = ask("Question 2 - What did peugeot make before it made cars\na. Bicycles\nb. Pepper grinders\nc. Corsets\nd. Ammunition\ne. All of the above\n", ['a', 'b', 'c', 'd', 'e'])
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

q3 = ask("Question 3 - What car holds the lap record for the Nurburgring\na. Ferrari Laferrari\nb. Bughatti Chiron\nc. Porche 919 Hybrid\nd. Mercedes W12 Formula 1 car\n", ['a', 'b', 'c','d'])
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

q4 = ask("Question 4 - When was the first car made\na. 1873\nb. 1886\nc. 1904\nd. 1914\n", ['a', 'b', 'c','d'])
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

q5 = ask("Question 5 - Which car has the fastest accelaration\na. BMW M5\nb. Audi RS5\nc. Mercedes c300\n", ['a', 'b', 'c'])
if q5 == "a":
    score = score + 5
if q5 == "b":
    score = score
if q5 == "c":
    score = score
else:
    score = score

q6 = ask("Question 6 - What car won the last Bathurst race\na. Holden commodore VX\nb. Ford mustang MK6\nc. Holden commodore ZB\n", ['a', 'b', 'c'])
if q6 == "a":
    score = score
if q6 == "b":
    score = score + 5
if q6 == "c":
    score = score
else:
    score = score

q7 = ask("Question 7 - What car company owns Porche\na. Maserati\nb. Audi\nc. Mercedes\nd. Volkswagen\n", ['a', 'b', 'c','d'])
if q7 == "a":
    score = score
if q7 == "b":
    score = score
if q7 == "c":
    score = score
if q7 == "d":
    score = score + 5
else:
    score = score

q8 = ask("Question 8 - Which car will win in a quarte mile drag race\na. Porche 918 Spyder\nb. Mclaren P1\nc. Ferrari Laferrari", ['a', 'b', 'c'])
if q8 == "a":
    score = score
if q8 == "b":
    score = score
if q8 == "c":
    score = score + 5
else:
    score = score

q9 = ask("Question 9 - Which car has a higher top speed\na. 1991 Bughatti EB110 SS\nb. 1994 Toyota Supra\nc. 1970 Porche 917", ['a', 'b', 'c'])
if q9 == "a":
    score = score
if q9 == "b":
    score = score
if q9 == "c":
    score = score + 5
else:
    score = score

q10

