# imports
import time
import random
score = 0

print("\n\nWelcome to the epic car quiz")
print("\nPlease asnswer each question in lower case Eg. a, b, c") # TODO take care of this yourself rather than relying on the user



def ask(question, answers):
    #TODO - docstring
    ''' ask fuction that doesent allow other answers '''
    response = None
    while response not in answers:
        response = input(question)
        if response not in answers:
            print ("\nPlease input an actual answer")
    return response



#list of questions    
questions = [
    {'question':"What is faster in a quarter mile drag race\na. Porche 911 GT3 RS\nb. Honda Acura NSX\nc. Lamborghini Countach\n", "options":['a', 'b', 'c'], "correct":'a'},
    {'question':"What did peugeot make before it made cars\na. Bicycles\nb. Pepper grinders\nc. Corsets\nd. Ammunition\ne. All of the above\n", "options":['a', 'b', 'c', 'd', 'e'], "correct":'e'},
    {'question':"What car holds the lap record for the Nurburgring\na. Ferrari Laferrari\nb. Bughatti Chiron\nc. Porche 919 Hybrid\nd. Mercedes W12 Formula 1 car\n", "options":['a', 'b', 'c', 'd'], "correct":'c'},
    {'question':"When was the first car made\na. 1873\nb. 1886\nc. 1904\nd. 1914\n", "options":['a', 'b', 'c','d'], "correct":'b'},
    {'question':"Which car has the fastest accelaration\na. BMW M5\nb. Audi RS5\nc. Mercedes c300\n", "options":['a', 'b', 'c'], "correct":'a'},
    {'question':"What car won the last Bathurst race\na. Holden commodore VX\nb. Ford mustang MK6\nc. Holden commodore ZB\n", "options":['a', 'b', 'c'], "correct":'b'},
    {'question':"What car company owns Porche\na. Maserati\nb. Audi\nc. Mercedes\nd. Volkswagen\n", "options":['a', 'b', 'c','d'], "correct":'d'},
    {'question':"Which car will win in a quarte mile drag race\na. Porche 918 Spyder\nb. Mclaren P1\nc. Ferrari Laferrari\n", "options":['a', 'b', 'c'], "correct":'c'},
    {'question':"Which car has a higher top speed\na. 1991 Bughatti EB110 SS\nb. 1994 Toyota Supra\nc. 1970 Porche 917\n", "options":['a', 'b', 'c'], "correct":'c'},
    {'question':"Which of these manufacturers is NOT Fremch\na. Bugatti\nb. Renault\nc. Peageot\nd. Fiat\ne. Citroen\n", "options":['a', 'b', 'c', 'd', 'e'], "correct":'d'},
    {'question':"What car manufacturer has the most WRC victories\na. Audi\nb. Lancia\nc. Subaru\nd. Ford\n", "options":['a', 'b', 'c','d'], "correct":'b'},
    {'question':"Who is the first driver for the Alpha Tauri Formula 1 team\na. Pierre Gasly\nb. Max Verstappen\nc. Lewis Hamilton\n", "options":['a', 'b', 'c'], "correct":'a'},
    {'question':"What Formula 1 team is the current reighning champion\na. Alpha Tauri\nb. Red Bull\nc. Mercedes\nd. Ferrari\n", "options":['a', 'b', 'c','d'], "correct":'c'},
    {'question':"What does BMW stand for\na. Bayerische Motoren Werke\nb. Berlin Motor Wagons\nc. Brandenburg machten Wehrmacht\n", "options":['a', 'b', 'c'], "correct":'a'},
    {'question':"Which manufacturer makes the Charger\na. Ford\nb. Dodge\nc. Chevrolet\n", "options":['a', 'b', 'c'], "correct":'b'},
    {'question':"What kind of engine does a mlcaren P1 have\na. v12\nb. v10\nc. Hybrid V8\nd. Hybrid v12 with Kinetic energy recovery system\n", "options":['a', 'b', 'c','d'], "correct":'c'},
    {'question':"What is the most expensive car to buy from the manufacturer\na. Pagani Zonda\nb. BugattiLa Voiture Noire\nc. Mclaren Senna\n", "options":['a', 'b', 'c'], "correct":'b'},
    {'question':"What is the estimated price for the soon to be released Rolls Royce Boat Tail\na. $38 Million\nb. $31 Million\nc. $27 Million\nd. $18.7 Million\n", "options":['a', 'b', 'c','d'], "correct":'a'},
    {'question':"What was the best race in motorsport\na. 90's Formula 1\nb. Le Mans\nc. Groub B rally\n", "options":['a', 'b', 'c'], "correct":'c'},
    {'question':"Which car company is from the Czech Republic\na. Dacia\nb. Volvo\nc. Saab\nd. Skoda\n", "options":['a', 'b', 'c','d'], "correct":'d'}
]

qnumber = 1

random.shuffle(questions)
# marks questions
for question in questions:
    response = ask(question['question'], question['options'])
    if response == question['correct']:
        score += 5

#scoring system 
print (f"you scored {score}%")
if score >= 90:
    grade = "A+"
elif score >= 80:
    grade = "A"
elif score >= 70:
    grade = "B"
elif score >= 60:
    grade = "C"
elif score >= 50:
    grade = "D"
elif score >= 30:
    grade = "E"
elif score >= 0:
    grade = "F"

print(grade)
 
# os.system("ls")gvb
# os.system('clear')

# TODO
# ask quesrtions in a defferent order each time
# put the correct ans in a different place each time
# allow user to play again