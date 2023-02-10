

number = 5
#while number <10:
#    print(number)
#__________________________________________
while number <10:
    number+=1
    print(number)
#__________________________________________

users=["ali","akbar","reza"]

varify = []

while users:
    user = users.pop()
    varify.append(user)

    print(varify)
###############################################################################

pets = ["dog","cat","bird","spider","sheep","cat","cow","rost","pig","cat","elephant","cat","wal","cat"]

while "cat" in pets:
    pets.remove("cat")
print(pets)