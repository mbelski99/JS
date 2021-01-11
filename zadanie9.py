try:
    txt = open('plik.txt', 'r')
except (IOError, ZeroDivisionError) as a:
 print(a)
 if txt:
    print(txt.closed)
try:
    txt1= open('plik1.txt', 'w+')
except (IOError, ZeroDivisionError) as b:
 print(b)
 if txt1:
    print(txt1.closed)
for line in txt.readlines():
    txt1.writelines(line)