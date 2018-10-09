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

    films = {"Race": [12, 25, 200],
             "Ant-Man": [16, 25, 300],
             "Deadpool": [18, 18, 180],
             "Infinity-War": [12, 29, 400],
             "Stranger Things 3": [3, 10, 350],
             "Game of thorns": [18, 10, 350],
             }

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

        d1 = {"1420101": {"email_id": "varsha", "password": "12345"},
              "1420102": {"email_id": "jerry", "password": "34567"},
              "1420103": {"email_id": "tommy", "password": "143567"},
              "1420104": {"email_id": "harley", "password": "12513783"},
              "1420105": {"email_id": "admin", "password": "admin"},
              "1420107": {"email_id": "a", "password": "a"}}
        for i in d1:
            if (username == "admin") and (password == "admin"):
                self.adminSec()

                break
            elif(username == d1[i]['email_id']) and (password == d1[i]['password']):
                self.movies()
                break
            else:
                wrong = Tk()
                wrong.geometry("200x80")
                label = Label(wrong, text="Wrong password or username", font=("arial", 8, "bold")).pack()
                wrong.mainloop()
    def adminSec(self):
        admin=Tk()
        label=Label(admin,text="Enter movie name").grid(row=0,column=0)
        entry1=Entry(admin)
        entry1.grid(row=0,column=1)
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
            answer=tkinter.messagebox.askyesno(title="Procced", message="Do you want proceed further to buy tkickets")
            print("Great,  price of a ticket is {}  .".format(self.films[self.selectedMovie.strip().title()][2]))
            # proceeding further for purchasing

        if answer:
            procced2=Tk()
            self.label=Label(procced2,text="Enter the number of ticket you want to buy").grid(row=0,column=0)
            self.entry = Entry(procced2)
            self.entry.grid(row=0,column=1)
            but=Button(procced2,text="GO",command=self.info)
            but.grid(row=1,column=1)

            # amount = self.entry.get()
            # print(amount)
            procced2.mainloop()

    def addUser(self):
        addUser= Tk()
        addUser.geometry("400*400")
        label = Label(addUser, Text="Enter user name").grid(row=1,column=0)
        entry1 = Entry(addUser).grid(row=2,column=0)
        label2 = Label(addUser, Text="Enter user name").grid(row=2,column=0)
        entry2 = Entry(addUser).grid(row=2,column=0)

        btn = Button(addUser ,Text="Add user").grid(row=3,column=1)


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
        # elif getint(age) < films[self.selectedMovie.strip().title()][0]:
        #     print("Sorry , you are too yong to watch this movie.")
        # elif self.selectedMovie.strip().title() is not films:
        #     print("Sorry, this movie is not available please try again.")
        #     print(self.selectedMovie.strip().title())


root = Tk()
p = project(root, 0)
root.mainloop()
