import random

#0
print("egy név generálása")

vnevek=["Ádám", "Balogh", "Lakatos", "Tóth", "Rézműves", "Váradi"]
férfiKnevek=["András", "Béla", "Géza", "József", "István"]
noiKnevek=["Anita", "Ildikó", "Erika", "Mariann"]

#1.
neme=input("Kérem a neveket (férfi/női):")

if neme.lower()=="férfi":
    teljesnev = random.choice(vnevek)+' '+random.choice(férfiKnevek)
elif neme.lower()=="nő":
    teljesnev = random.choice(vnevek)+' '+random.choice(noiKnevek)
else:
    print("rossz nevet adott meg")
    exit()

#2-3
print(teljesnev)