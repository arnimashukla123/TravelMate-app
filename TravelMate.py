trains = [
    [101, "RAJDHANI EXPRESS", "DELHI", 1200, 23],
    [123, "SAMAY", "MUMBAI", 4500, 12],
    [345, "VANDE BHARAT", "BANGLORE", 3000, 32]
]
buses = [
    [450, "VOLVO", "DELHI", 800, 20],
    [567, "SHATABDI", "MUMBAI", 500, 15],
    [789, "NUEGO", "BANGLORE", 1000, 25]
]
train_passenger = []
bus_passenger = []

def add_trainticket():
    train_number = int(input("Enter train number: "))
    train_name = input("Enter train name: ")
    train_destination = input("Enter train destination: ")
    train_price = int(input("Enter ticket price: "))
    train_seat = int(input("Enter seats available: "))
    train_ticket = [train_number,train_name,train_destination,train_price,train_seat]
    trains.append(train_ticket)
    print("Train ticket added successfully!")

def add_busticket():
    bus_number = int(input("Enter bus number: "))
    bus_name = input("Enter bus name: ")
    bus_destination = input("Enter bus destination: ")
    bus_price = int(input("Enter ticket price: "))
    bus_seat = int(input("Enter seats available: "))
    bus_ticket = [bus_number,bus_name,bus_destination,bus_price,bus_seat]
    buses.append(bus_ticket)
    print("Bus ticket added successfully!")

def edit_trainticket():
    train_id = int(input("Enter train number to update: "))
    for train in trains:
        if train[0] == train_id:
            print("Enter new details")
            train[0] = int(input("Enter train number: "))
            train[1] = input("Enter train name: ")
            train[2] = input("Enter train destination: ")
            train[3] = int(input("Enter ticket price: "))
            train[4] = int(input("Enter seats available: "))
            print("Train ticket updated successfully!")
        else:
            print("Train not found.")

def edit_busticket():
    bus_id = int(input("Enter bus number to update: "))
    for bus in buses:
        if bus[0] == bus_id:
            print("Enter new details")
            bus[0] = int(input("Enter bus number: "))
            bus[1] = input("Enter bus name: ")
            bus[2] = input("Enter bus destination: ")
            bus[3] = int(input("Enter ticket price: "))
            bus[4] = int(input("Enter seats available: "))
            print("Bus ticket updated successfully!")
        else:
            print("Bus not found.")

def book_trainticket():
    destination = input("Enter your destination: ")
    for train in trains:
        if train[2].lower() == destination.lower():
            print("Train number:", train[0])
            print("Train name:", train[1])
            print("Destination:", train[2])
            print("Ticket price:", train[3])
            print("Seats available:", train[4])
            customer_id = input("Enter your ID: ")
            people = int(input("Number of people: "))
            if people <= 0:
                print("Invalid number of people.")
                return
            if people > train[4]:
                print("Sorry, not enough seats available.")
                return
            total_amount = train[3] * people
            for i in range(people):
                name = input("Enter name: ")
                age = int(input("Enter age: "))
                passenger = [customer_id,name,age,train[0],train[1],train[2],total_amount]
                train_passenger.append(passenger)
            train[4] = train[4] - people
            print("--------------------------------")
            print("CONGRATULATIONS")
            print("Ticket booked successfully!")
            print("Total amount:", total_amount)
            print("Remaining seats:", train[4])
            print("--------------------------------")
    print("Train not available for this destination.")

def book_busticket():
    destination = input("Enter your destination: ")
    for bus in buses:
        if bus[2].lower() == destination.lower():
            print("Bus number:", bus[0])
            print("Bus name:", bus[1])
            print("Destination:", bus[2])
            print("Ticket price:", bus[3])
            print("Seats available:", bus[4])
            customer_id = input("Enter your ID: ")
            people = int(input("Number of people: "))
            if people <= 0:
                print("Invalid number of people.")
                return
            if people > bus[4]:
                print("Sorry, not enough seats available.")
                return
            total_amount = bus[3] * people
            for i in range(people):
                name = input("Enter name: ")
                age = int(input("Enter age: "))
                passenger = [customer_id,name,age,bus[0],bus[1],bus[2],total_amount]
                bus_passenger.append(passenger)
            bus[4] = bus[4] - people
            print("--------------------------------")
            print("CONGRATULATIONS")
            print("Ticket booked successfully!")
            print("Total amount:", total_amount)
            print("Remaining seats:", bus[4])
            print("--------------------------------")
    print("Bus not available for this destination.")

def view_ticket():
    customer_id = input("Enter your ID to view ticket details: ")
    found = False
    for passenger in train_passenger:
        if passenger[0].lower() == customer_id.lower():
            found = True
            print("\n---------- TRAIN TICKET ----------")
            print("Passenger name:", passenger[1])
            print("Passenger age:", passenger[2])
            print("Train number:", passenger[3])
            print("Train name:", passenger[4])
            print("Train destination:", passenger[5])
            print("Total amount:", passenger[6])
    for passenger in bus_passenger:
        if passenger[0].lower() == customer_id.lower():
            found = True
            print("\n---------- BUS TICKET ----------")
            print("Passenger name:", passenger[1])
            print("Passenger age:", passenger[2])
            print("Bus number:", passenger[3])
            print("Bus name:", passenger[4])
            print("Bus destination:", passenger[5])
            print("Total amount:", passenger[6])
    if found == False:
        print("No ticket found for this ID.")

def menu1():
    while True:
        print("************************************************************************************")
        print("                              TICKET MASTER MENU")
        print("************************************************************************************")
        print("1: Add train ticket")
        print("2: Add bus ticket")
        print("3: Edit train ticket")
        print("4: Edit bus ticket")
        print("5: Exit")
        print("************************************************************************************")
        choice = int(input("Enter the choice: "))
        if choice == 1:
            add_trainticket()
        elif choice == 2:
            add_busticket()
        elif choice == 3:
            edit_trainticket()
        elif choice == 4:
            edit_busticket()
        elif choice == 5:
            break
        else:
            print("Invalid input")

def menu2():
    while True:
        print("************************************************************************************")
        print("                              TICKET BOOKER MENU")
        print("************************************************************************************")
        print("1: Book train ticket")
        print("2: Book bus ticket")
        print("3: View tickets")
        print("4: Exit")
        print("************************************************************************************")
        choice1 = int(input("Enter the choice: "))
        if choice1 == 1:
            book_trainticket()
        elif choice1 == 2:
            book_busticket()
        elif choice1 == 3:
            view_ticket()
        elif choice1 == 4:
            break
        else:
            print("Invalid input")

def choose_yourself():
    while True:
        print("************************************************************************************")
        print("                              DISPLAY MENU")
        print("************************************************************************************")
        print("1. TICKET MASTER")
        print("2. TICKET BOOKER")
        print("3. EXIT")
        print("************************************************************************************")
        choice2 = int(input("Enter your choice: "))
        if choice2 == 1:
            menu1()
        elif choice2 == 2:
            menu2()
        elif choice2 == 3:
            print("Thank you for using TravelMate!")
            break
        else:
            print("Invalid choice. Please try again.")
print("************************************************************************************")
print("                               TravelMate")
print("************************************************************************************")
choose_yourself()
