import random

#0
print("osztályzatok generálása")

#1.
db = int(input("kérem az osztályzatok számát:"))

osztályzatok = []
#mivel ismerjük a darabok számát - ezért a generálást előre meghatározott lépésszámú ciklusban végezzükk
for i in range(db):
    oszt = random.randint(1,5)
    osztályzatok.append(oszt)

#2-3
print(osztályzatok)