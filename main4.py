import random

#0
print("egy osztály tanulóinak generálása")

vnevek=["Ádám", "Balogh", "Lakatos", "Tóth", "Rézműves", "Váradi"]
férfiKnevek=["András", "Béla", "Géza", "József", "István"]
noiKnevek=["Anita", "Ildikó", "Erika", "Mariann"]

db=int(input("Kérem a tanulók számát"))
tanulok = []
for i in range(db):
    #tanuló neve
    neme=random.randint(1,2)
    if neme==1:
        teljesnev = random.choice(vnevek)+' '+random.choice(férfiKnevek)
        neme="férfi"
    elif neme.lower()=="nő":
        teljesnev = random.choice(vnevek)+' '+random.choice(noiKnevek)
        neme="nő"
    #tanuló születési ideje
    # ev=random.randint(2000, 2050)
    honap=random.randint(1, 12)
    nap=random.randint(1, 28)

    datum= f"{ev}.{honap:0>2d}.{nap:0>2d}"    
    #magasság
    magassag=random.randint(155, 190)

    #tanuló összeállítása
    tanulo = (teljesnev,datum,neme,magassag)

    #felvétel a tanulókhoz
    tanulok.append(tanulo)

#2-3
for item in tanulok:
    print(item)
