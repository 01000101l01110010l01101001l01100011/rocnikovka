#!/usr/bin python
import os
import subprocess
import sys

minimum = 27000
maximum = 54000
try:
    if sys.argv[1]=="min":
        print(f'Minimum je: {minimum} znaků')

    if sys.argv[1]=="max":
        print(f'Maximum je: {maximum} znaků')
except:
    pass

words = subprocess.run(
    ["pdftotext main.pdf - | wc -w"],
    capture_output = True,
    text=True,
    shell=True
    ).stdout.strip("\n")

characters = subprocess.run(
     ["pdftotext main.pdf - | wc -c"],
    capture_output = True,
    text=True,
    shell=True
).stdout.strip("\n")

words= int(words)
characters = int(characters)

print(f'Máš {words} slov')

if characters <= minimum:
    print(f'Jsi v {int((characters/minimum)*100)} % minima')
    print(f'zbývá ti už jen {minimum-characters} znaků to zvládneš!')

elif characters <= maximum:
    print(f'Jsi v pohodě. Ale bacha můžeš napsat už jen {maximum-characters} znaků')

elif characters > maximum:
    print(f'fůůůj šprte. máš {int((characters/maximum)*100)} % maxima trochu to klidni')


def gto(num:int):
    if num>0:
        return num
    else:
        return 0

min_bar=f'█'*int((characters/minimum)*50) + "-"*(50-(int((characters/minimum)*50)))
max_bar=f'█'*int((gto(characters-minimum)/maximum)*50) + "-"*(50-(int((gto(characters-minimum)/maximum)*50)))
print(f'\r |{min_bar}|{max_bar}| \r')


troling = False
for s in str(characters):
    if s =="6":
        troling=True
    if s=="9" and troling:
        print("Někdě v čísle tvých znaků je 69 a to je nice")

trolenicko = False
for s in str(words):
    if s =="6":
        troling=True
    if s=="9" and trolenicko:
        print("Někdě v čísle tvých slov je 69 a to je nice")      


