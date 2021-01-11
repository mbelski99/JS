bridge_of_death = '''
-Jaki jest twój ulubiony kolor?
-Niebieski!
-Dobrze. Idź.

-Stój. Jakie jest twe imię?
-Sir Galahad z Camelotu.
-Jaki jest twój cel?
-Odnaleźć Graala.
-Jaki jest twój ulubiony kolor?
-Niebieski... nie... żóóóółtyyyy!
'''
sl=0
li=0
x=0
for a in bridge_of_death:
    a=a.lower()
    if a.isalpha():
        li+=1
    if li>=4 and x==0:
        li=0
        sl+=1
        x=1
    if a.isalpha()!=1:
        li=0
        x=0
print(sl)