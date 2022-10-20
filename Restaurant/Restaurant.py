Rice_With_Chicken = int(5)
Chicken_soup = int(5)
Stuffed_peppers = int(5)
Fish = int(5)
coca_cola = int(5)
Iced_tea = int(5)
Dessert = int(5)
c1v = 0
c2v = 0
c3v = 0
c4v = 0
c5v = 0
c6v = 0
c7v = 0
password = 1234
c1 = " Rice with chicken,",float(10)
c2 = " Chicken Soup,",float(10)
c3 = " Stuffed peppers,",float(10)
c4 = " Fish,",float(10)
c5 = " Coca Cola,",float(2)
c6 = " Iced tea,",float(2)
c7 = " Dessert,",float(5)
while(True):
    print("Welcome to the command interactive menu, please introduce your order command to start, to finish just type 'pay' to finish your order.If you do not know any command, type in 'help'")
    Result = 0
    Food = " "
    while(True):
        option = input()
        if option == "c1" :
            if Rice_With_Chicken >= 1:
                Result = Result + c1[-1]
                c1v += 1
                Rice_With_Chicken -= 1
                if Food.count(" Rice with chicken,") <= 0:
                    Food = Food + c1[0]                    
            else:
                print("We do not have any more rice with chicken!")
        elif option == "c2":
            if Chicken_soup >= 1:                
                Result = Result + c2[-1]
                if Food.count(" Chicken Soup,") <= 0:
                    Food = Food + c2[0]
                c2v += 1
                Chicken_soup -= 1
            else:
                print("We do not have any more chicken soup!")
        elif option == "c3":
            if Stuffed_peppers >= 1:
                Result = Result + c3[-1]
                if Food.count(" Stuffed peppers,") <= 0:
                    Food = Food + c3[0]
                c3v += 1
                Stuffed_peppers -= 1
            else:
                print("We do not have any more stuffed peppers!")
        elif option == "c4" :
            if Fish >= 1:
                Result = Result + c4[-1]
                if Food.count(" Fish,") <= 0 :
                    Food = Food + c4[0]
                c4v += 1
                Fish -= 1
            else:
                print("We do not have any more fish!")
        elif option == "c5" :
            if coca_cola >= 1:
                Result = Result + c5[-1]
                if Food.count(" Coca cola,") <= 0:
                    Food = Food + c5[0]
                c5v += 1
                coca_cola -= 1
            else:
                print("We do not have any more Coca-cola!")
        elif option == "c6" :
            if Iced_tea >= 1:
                Result = Result + c6[-1]
                if Food.count(" Iced tea,") <= 0:
                    Food = Food + c6[0]
                Iced_tea -= 1
                c6v += 1
            else:
                print("We do not have any more iced tea!")
        elif option == "c7" :
            if Dessert >= 1:
                Result = Result + c7[-1]
                if Food.count(" Dessert,") <= 0:
                    Food = Food + c7[0]
                Dessert -= 1
                c7v += 1
            else:
                print("We do not have any more deserts!")
        elif option == "help":
                print("""The commands are:
                c1 : Rice with chicken.
                c2 : Chicken Soup.
                c3 : Stuffed peppers.
                c4 : Fish.
                c5 : Coca cola.
                c6 : Iced tea.
                c7 : Dessert.
                pay : To complete and pay your order.
                manage : To open the management options
                I hope they help!!""")
        elif option == "pay" :
            print("Your orders were the following:",Food," your total is: ",Result,"Dollars, and after taxes",(Result*0.0665+Result)," dollars, have a great day!")
            break
        elif option == "manage":           
            if password == int(input("Type in the password")):
                print("""Commands for management
                Type 'inventory' to update the inventory
                Type 'sales' to know how many sales were made by product
                Type 'refill' to receive more items on the inventory
                Type 'reset' to reset all the sales made!
                Type 'exit' to go back to ordering""")
                while(True):
                    option = input()                   
                    if option == "refill":
                        Rice_With_Chicken += int(input("Type how many rice with chicken can be made"))
                        Chicken_soup += int(input("Type how many chicken soups can be made"))
                        Stuffed_peppers += int(input("Type how many stuffed peppers can be made"))
                        Fish += int(input("Type how many fish's can be made"))
                        coca_cola += int(input("Type in how many Coca-Cola's were received"))
                        Iced_tea += int(input("Type in how many Iced Teas were received"))
                        Dessert += int(input("Type how many desserts were received"))
                        print("You have finished with the receiving of products")
                    elif option == "sales":
                        print("We sold ",c1v,"Rice with chicken.")
                        print("We sold ",c2v,"Chicken soups.")
                        print("We sold ",c3v,"Stuffed peppers")
                        print("We sold ",c4v,"Fish's")
                        print("We sold ",c5v,"Coca Cola's")
                        print("We sold ",c6v,"Iced tea's")
                        print("We sold ",c7v,"Desserts")
                    elif option == "inventory":
                        Rice_With_Chicken = int(input("Rice with chicken"))
                        Chicken_soup = int(input("Chicken soups"))
                        Stuffed_peppers = int(input("Stuffed pepperss"))
                        Fish = int(input("Fish's"))
                        coca_cola = int(input("Coca Cola's"))
                        Iced_tea = int(input("Iced tea's"))
                        Dessert = int(input("Desserts"))
                        print("You have finished updating the inventory")
                    elif option == "reset":
                        c1v = 0
                        c2v = 0
                        c3v = 0
                        c4v = 0
                        c5v = 0
                        c6v = 0
                        c7v = 0
                        print("All sales have been reseted!")
                    elif option == "exit":
                        print("You can now continue making orders!")
                        break
                    else:
                        print("Unknown command")
        else:
            print("Unknown command, if you need help you can type 'help'")