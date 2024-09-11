# Making List with message and len ()
vehicle=['Hell cat', 'Suzuki', 'Aston Martin']
Transportation=len(vehicle)
print(Transportation)
print(vehicle)
#Add to List
vehicle.insert(0, 'Corvette')
vehicle.insert(1, 'Mustang')

v=vehicle[0].title()
print(v+' Is one freak of a car ')

v=vehicle[1].title()
print(v+' Is a car i want')

v=vehicle[2].title()
print(v+' is personally my dream car')

v=vehicle[7].title()
print(v+' A motorcycle i would like to have')
#it should be v=vehicle[3] not 7
v=vehicle[5].title()
print(v+'Is also one of my choices because of James Bond ')
# It Should be v=vehicle[4] not 5
vehicle.append('Dirt Bike')
print(vehicle)

#dont Like this car anymore
del(vehicle[1])
vehicle.insert(0, 'Camaro')
print(vehicle)

# Car got wrecked
t=vehicle.pop(1)
print(t.title() + ' was rear ended')

del(vehicle[1])
print(vehicle)
print('all other car is ok')

# sort List
vehicle.sort()
print(vehicle)

vehicle.sort(reverse=True)
print(vehicle)

vehicle=['Camaro', 'Suzuki', 'Aston Martin', 'Dirt Bike']
print(' This was the original list ')
print(vehicle)










