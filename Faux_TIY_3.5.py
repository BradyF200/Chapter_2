invite=['keanu reeves','post malone','john cena']

invite[1]='seth rollins'
print(invite)

invite_1=f"Dear {invite[0].title()}. I would like to invite you to a diner party"
print(invite_1)
invite2=f'Dear {invite[1].title()}. I would like you to join Our dinner party'
print(invite2)
invite3=f'Dear {invite[2].title()}. Please join the party'
print(invite3)

invite[1]='seth rollins'
print(invite)

print(f'post malone could not make it to the party')