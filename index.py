films = {
    "Race 3": [12, 25, 200],
    "Ant-Man": [16, 25, 300],
    "Deadpool 2": [18, 18, 180],
    "Infinity-War": [12, 29, 400],
    "Stranger Things 3": [3, 10, 350],
}

users = {

    1: {
        "username": "admin",
        "password": "admin"
    },
    2: {
        "username": "varsha",
        "password": "varsha062"
    },
    3: {
        "username": "sakshi",
        "password": "memelover"
    },
    4: {
        "username": "jhanvi",
        "password": "pizzalover"
    },
    5: {
        "username": "aastha",
        "password": "asslover"
    },
}


def addMovie():
    key = input("Enter movie name")
    age = input("Enter min age")
    ticketAvail = input("Enter number tickets")
    price = input("Enter amount of ticket")
    films[key] = [age, ticketAvail, price]


# Selection of movie
def processTicketBooking():
    def movieChoice():
        for key in films.keys():
            print(key)

    movieChoice()
    choice = input("\nEnter Movie name: ").strip().title()
    if choice in films:
        age = int(input("Enter yor age:\n"))

        # verifying age
        if age >= films[choice][0]:
            print("Great,  price of a ticket is {}  .".format(films[choice][2]))
            choice2 = input("Do you want proceed further to buy thickets ?(y/n) ").strip().lower()

            # proceeding further for purchasing
            if choice2 == 'y':

                # asking amount of tickets
                amount = int(input("Enter number of tickets you want to buy :\n"))
                if amount <= films[choice][1]:
                    # calculating total amount of bill
                    billAmount = amount * films[choice][2]
                    print("Your total bill for {} thickets is {}".format(amount, billAmount))
                    # If ticket are less available tickets
                elif amount > films[choice][1]:
                    print("Sorry we have only {} tickets available".format(films[choice][1]))
            elif choice2 == 'n':
                print("Thank you for visiting us !")

        elif age < films[choice][0]:
            print("Sorry , you are too yong to watch this movie.")
    elif choice is not films:
        print("Sorry, this movie is not available please try again.")


def registerUser():
    i = 6
    users[i] = {}
    users[i]["username"] = input("Enter username ")
    users[i]["password"] = input("Enter password")


# addUser()

def userLogin():
    username = input("Your username")
    password = input("password")
    for keys in users:
        if users[keys]["username"] == "admin" and users[keys]["password"] == "admin":
            addMovie()
            break
        elif users[keys]["username"] == username and users[keys]["password"] == password:
            processTicketBooking()
            break
        else:
            print("User not found \n Make an account now!")
            registerUser()
            break


userLogin()


def deleteUser():
    username = input("Your username")
    password = input("password")
    for keys in users:
        if users[keys]["username"] == username and users[keys]["password"] == password:
            print("USer Found")
            stop = keys
            print(stop)
            del users[stop]
            break
