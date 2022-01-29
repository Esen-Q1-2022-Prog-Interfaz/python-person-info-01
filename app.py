from db import createNewPersonCard, getPersonById, getAllPersonCards, updatePersonCard, deletePersonCard


def showMenu():
    print()
    print()
    optionDict = {
        " 0": "create a new person card",
        " 1": "search a person card by id",
        " 2": "show all person cards",
        " 3": "update a person card",
        " 4": "delete a person card",
        "-1": "exit app",
    }
    for option, value in optionDict.items():
        print(f"{option}:: {value}")
    print()


while True:
    showMenu()
    option = int(input("option: "))
    if option == -1:
        """exit app"""
        break
    elif option == 0:
        """create a new person card"""
        print()
        name = input("name: ")
        age = int(input("age: "))
        salary = int(input("salary: "))
        createNewPersonCard(name, age, salary)
    elif option == 1:
        """search person by id"""
        id = int(input("id to search: "))
        personCardDict = getPersonById(id)
        print(personCardDict)
        print()
    elif option == 2:
        """show all person cards"""
        personCardList = getAllPersonCards()
        for card in personCardList:
            print(card)
    elif option == 3:
        """update person card"""
        id = int(input("id of card to update: "))
        personCardDict = getPersonById(id)
        print(personCardDict)
        updateOption = int(input("are you sure to update this card? (0=no, 1=yes): "))
        if updateOption:
            name = input("name: ")
            age = int(input("age: "))
            salary = int(input("salary: "))
            updatePersonCard(id, name, age, salary)
        else:
            print("update canceled")
    elif option == 4:
        """delete a person card"""
        id = int(input("id of card to delete: "))
        personCardDict = getPersonById(id)
        print(personCardDict)
        deleteOption = int(input("are you sure to delete this card? (0=no, 1=yes): "))
        if deleteOption:
            deletePersonCard(id)
        else:
            print("delete canceled")
    else:
        print("app just continues...")
