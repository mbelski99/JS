word="Słowo"
x=0
while x<5:
    word1=input('Wpisz słowo:')
    if word1!=word:
        print ("Źle! Spróbuj jeszcze raz!!!")
    else:
        print ("Gratulacje :D")
        break
    x+=1
if x==5:
    print ("Koniec prób!")