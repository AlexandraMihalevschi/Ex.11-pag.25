x = []
a = int(input("Scrieti numarul de elemente:"))

for i in range(0, a):
    element = int(input('Scrieti un numar:'))
    x.append(element)
     
print("Acesta este sirul creat",x, end="\n")
print("A: afişează pe ecran componentele tabloului la un interval de 5 poziţii")
print(x[0], x[1], x[2], x[3], x[4])

print("B: afişează pe ecran numerele în ordinea inversă a introducerii în calculator")
print(x[::-1])

print("C: sortează componentele tabloului în ordine descrescătoare")
y=x
y.sort(reverse = True)
print(y)

print("""D: afişează pe ecran doar componentele pare""")
z = []
s = 0
n = 0
for i in x:
    if i%2==0:
        print(i, end=" ")
        s = s+i
        n += 1
        z.append(i)

print("""
E: afişează pe ecran media aritmetică a componentelor pare""")
print(s/n)

print("F:  afişează pe ecran doar componentele impare")
for i in x:
    if i%2!=0:
        print(i, end=" ")

print("""
G:  afişează pe ecran doar componentele care sunt mai mari ca x şi nu sunt
divizibile cu y""")
x1= int(input("Dati x: "))
y= int(input("Dati y: "))
for i in x:
    if (i > x1) and (i % y!= 0):
        print(i, end=" ")

print("""
H:  afişează pe ecran doar componentele care sunt mai mari ca x şi mai mici
decât y""")
for i in x:
    if (i > x1) and (i < y):
        print(i, end=" ")

print("I: afişează pe ecran poziţiile (indicii) componentelor impare negative")
for i in x:
    if (i < 0) and (i % 2!= 0):
        print(x.index(i), end=" ")

print("J: afişează pe ecran poziţiile (indicii) componentelor ce conţin doar două cifre semnificative")
for i in x:
    if (i >= 10) and (i <= 99):
        print(x.index(i), end=" ")

print("K: înlocuieşte prima componentă a tabloului cu componenta de valoare minimă din tabloul respectiv ")
mn = min(x)
imn = x.index(min(x))
x0 = x[0]
del x[0]
del x[min(x)]
x.insert(0, mn)
print(x)
print("L: înlocuieşte componenta de valoare minimă din tabloul respectiv cu prima componentă a acestuia")
x.insert(imn, x0)
print(x)

print("""M: creează un tablou nou, format doar din componentele pare ale tabloului
introdus de la tastatură""")
print(z)

print("""N: creează un tablou nou, format doar din componentele divizibile cu 3 ale
tabloului introdus de la tastatură""")
k = []
for i in x:
    if i%3==0:
        k.append(i)
print(k)

print("""O: creează un tablou nou, format doar din acele componente ale 
tabloului introdus de la tastatură care au cel mult patru divizori""")
d1 = int(input("Dati un numar:"))
d2 = int(input("Dati un numar:"))
d3 = int(input("Dati un numar:"))
d4 = int(input("Dati un numar:"))
l = []
for i in x:
    if (i%d1==0) and (i%d2==0) and (i%d3==0) and (i%d4==0):
        l.append(i)
print(l)