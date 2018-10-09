import tkinter.messagebox
from tkinter import *


class project():
    username = "x"
    password = "x"
    selectedMovie = "x"
    age = "x"
    amount="x"
    key = [0]
    count = 0
    passwordR = ""
    usernameR= ""
    i = 1420108

    films = {"Race": [12, 25, 200],
             "Ant-Man": [16, 25, 300],
             "Deadpool": [18, 18, 180],
             "Infinity-War": [12, 29, 400],
             "Stranger Things 3": [3, 10, 350],
             "Game of thorns": [18, 10, 350],
             }
    users = {"1420101": {"email_id": "varsha", "password": "12345"},
          "1420102": {"email_id": "jerry", "password": "34567"},
          "1420103": {"email_id": "tommy", "password": "143567"},
          "1420104": {"email_id": "harley", "password": "12513783"},
          "1420105": {"email_id": "admin", "password": "admin"},
          "1420107": {"email_id": "a", "password": "a"}}

    def __init__(self, master, a):
        self.root = master
        self.e = a
        root.geometry("200x200")
        root.title("Login page")
        self.user1 = Label(root, text="Username").grid(row=0, column=0)
        self.uentry1 = Entry(root)
        self.uentry1.grid(row=0, column=1)


        self.passw = Label(root, text="Password").grid(row=1, column=0)
        self.pentry = Entry(root)
        self.pentry.grid(row=1, column=1)

        self.log = Button(root, text="Login", command=self.checkinfo).grid(row=3, column=1)

    def checkinfo(self):
        username = self.uentry1.get()
        password = self.pentry.get()


        for i in self.users:
            if (username == "admin") and (password == "admin"):
                self.adminSec()

                break
            elif(username == self.users[i]['email_id']) and (password == self.users[i]['password']):
                self.movies()
                break
            else:
                wrong = Tk()
                wrong.geometry("200x80")
                label = Label(wrong, text="Wrong password or username", font=("arial", 8, "bold")).grid(row=1,column=0)
                register=Button(wrong,text="Register now",command=self.addUser).grid(row=2,column=1)
                wrong.mainloop()
                break
    def adminSec(self):
        admin=Tk()
        admin.geometry("400x400")
        admin.title("Add movies by admin")
        self.label=Label(admin,text="Enter movie name").grid(row=0,column=0)
        self.entry1=Entry(admin)
        self.entry1.grid(row=0,column=1)
        self.label=Label(admin,text="Enter the min age").grid(row=1,column=0)
        self.entry2=Entry(admin)
        self.entry2.grid(row=1,column=1)
        self.label=Label(admin,text="Enter no of tickets").grid(row=2,column=0)
        self.entry3=Entry(admin)
        self.entry3.grid(row=2,column=1)
        self.label=Label(admin,text="Enter price of tickets").grid(row=3,column=0)
        self.entry4=Entry(admin)
        self.entry4.grid(row=3,column=1)
        self.btn= Button(admin,text="Add movie",command=self.addMoive).grid(row=4,column=1)
        admin.mainloop()

        #To latest movies
    def addMoive(self):
         movieName = self.entry1.get()
         minAge = self.entry2.get()
         numberOfTickets = self.entry3.get()
         ticketOfPrice = self.entry4.get()
         print(movieName,minAge,ticketOfPrice)
         self.films[movieName] = [minAge, numberOfTickets, ticketOfPrice]
         info = "{} is added successfully".format(movieName)
         tkinter.messagebox.showinfo(title="Movie added",message=info)


    def movies(self):
        movie = Tk()
        movie.title("Ticket Simulator")
        movie.geometry('500x400')
        label = Label(movie, text="MOVIES AVAILABEL", fg="black", font=('arial', 20, "bold"))
        label.grid(row=0, column=1)
        # spinbox1=Spinbox(root,from_=5,to=10,state=NORMAL).pack()
        count = 0
        for keys in self.films:
            self.count = Label(movie, text=keys, font=("arial", 10, "italic")).grid(row=count, column=0, sticky=W)
            count = count+1

        self.label = Label(movie, text="Enter movie name").grid(row=8, column=0)
        self.entry = Entry(movie)
        self.entry.grid(row=9, column=0)
        self.botton = Button(movie, text="Submit", command=self.processTicketBooking).grid(row=10, column=1)
        movie.mainloop()

    def processTicketBooking(self):
        selectedMovie = self.entry.get()
        self.selectedMovie = selectedMovie.strip().title()
        if selectedMovie.strip().title() in self.films:
            authority = Tk()
            authority.geometry("200x100")
            self.label = Label(authority, text="Enter your age: ").grid(row=0, column=0)
            self.ageentry = Entry(authority)
            self.ageentry.grid(row=0, column=1)
            self.button = Button(authority, text="Submit", command=self.agevarify).grid(row=1, column=1)
            authority.mainloop()



    def agevarify(self):

        age = self.ageentry.get()
        if getint(age) >= getint(self.films[self.selectedMovie.strip().title()][0]):
            info = "Great,  price of a ticket is {}  .".format(self.films[self.selectedMovie.strip().title()][2])
            answer=tkinter.messagebox.askyesno(title="Procced", message=info + "Do you want proceed further to buy tkickets")
            info = "Great,  price of a ticket is {}  .".format(self.films[self.selectedMovie.strip().title()][2])
            # proceeding further for purchasing
            if answer:
                procced2 = Tk()
                self.label = Label(procced2, text="Enter the number of ticket you want to buy").grid(row=0, column=0)
                self.entry = Entry(procced2)
                self.entry.grid(row=0, column=1)
                but = Button(procced2, text="GO", command=self.info)
                but.grid(row=1, column=1)

                # amount = self.entry.get()
                # print(amount)
                procced2.mainloop()
        elif getint(age) < getint(self.films[self.selectedMovie][0]):
            info = "Sorry , You are not eligible for {} , minimum age requirement is {}".format(self.selectedMovie , self.films[self.selectedMovie][0])
            tkinter.messagebox.showinfo(title="Not eligible" , message=info)



    def addUser(self):
        addUser= Tk()
        addUser.geometry("200x200")

        self.label = Label(addUser, text="Enter username").grid(row=0, column=0)
        self.myentry1 = Entry(addUser)
        self.myentry1.grid(row=0, column=1)
        self.label = Label(addUser, text="Enter the min age").grid(row=1, column=0)
        self.myentry2 = Entry(addUser)
        self.myentry2.grid(row=1,column=1)
        userNameR = self.myentry1.get()
        passwordR = self.myentry2.get()
        print(userNameR,passwordR)
        self.btn = Button(addUser ,text="Add user",command=self.addUserProcess).grid(row=3,column=1)
        addUser.mainloop()
    def addUserProcess(self):
        print("check")
        userNameR = self.myentry1.get()
        passwordR = self.myentry2.get()
        self.users[self.i] = {}
        self.users[self.i]["email_id"] = userNameR
        self.users[self.i]["password"] =passwordR
        self.i = self.i+1
        print(self.users)


    def info(self):

        info=Tk()
        # infoText = "Your total bill of tickets {} is {}".format()
        amount=self.entry.get()
        if getint(amount) <= getint(self.films[self.selectedMovie.strip().title()][1]):
                # calculating total amount of bill
                billAmount = getint(amount) * getint(self.films[self.selectedMovie.strip().title()][2])
                print("Your total bill for {} thickets is {}".format(amount, billAmount))

                # If ticket are less available tickets
        elif amount > self.films[self.selectedMovie.strip().title()][1]:
                print("Sorry we have only {} tickets available".format(self.films[self.selectedMovie.strip().title()][1]))
        infoText = "Your total bill of tickets {} is {}".format(amount, billAmount)
        label = Label(info, text=infoText).grid(row=0, column=0)


        info.mainloop()

root = Tk()
p = project(root, 0)
root.mainloop()
