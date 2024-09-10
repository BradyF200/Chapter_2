#Invatations
people=['keanu reeves','post malon','john cena']

J=people[0].title()
print(J + " im hosting a dinner party i would like you to attend")

J=people[1].title()
print(J + ' please join the party')

J=people[2].title()
print(J + " you are welcome to join the party")

J=people[1].title()
print(J + ' will not make it to  the party')

# A guest is sick
del(people[1])
people.insert(1, " Seth Freaking Rollins")

J=people[0].title()
print(J + " im hosting a dinner party i would like you to attend")

J=people[1].title()
print(J + ' please join the party')

J=people[2].title()
print(J + " you are welcome to join the party")


# More room
print('we got a bigger tabel')

people.insert(0, 'donald trump')
people.insert(2, 'Kendrick')
people.append('Jason')

J=people[0].title()
print(J + ' pary invite')

J=people[1].title()
print(J + " pary invite")

J=people[2].title()
print( J + " party invite")

J=people[3].title()
print(J + " party invite ")

J=people[4].title()
print(J + ' pary invite')

J=people[5].title()
print(J + ' pary invite')


#Shrink the list
print('I am only allowed to invite two people')
J=people.pop()
print( J.title() + ' sorry not invited')

J=people.pop()
print( J.title() + ' sorry not invited')

J=people.pop()
print( J.title() + ' sorry not invited')

J=people.pop()
print(J.title() + ' sorry you are as well kiced out')

#Still invited
J=people[0].title()
print(J + ' You are still welcome to come ')

J=people[1].title()
print( J + " you are also still invited")

#Del guest
del(people[1])
del(people[0])

print(people)











