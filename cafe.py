#define the menu of our food corner
menu ={
    "Pizza":40,
    "pasta":50,
    "Noodles":70,
    "Burger":30,
    "Shakes":30
}
print(menu)
#Great
print("Welcome our Jain's Food Corner")
print("pizza: RS40/n pasta: Rs50/n Noodles: RS30/n Burger: Rs30/n Shakes: RS30")

order_total = 0
#80 + 70 = 150

item_1 = input("enter your name of item you want to order now =")
if item_1 in menu:
    order_total += menu[item_1]#0 + 50
    print(f"your item{item_1}has been added to your order")
else:
    print(f"ordered item{item_1}is not avalaible yet")
    another_order = input("do you want to order another item?(yes/no)")
    if another_order == "yes":
        item_2 = input("enter the name of second item =")
        if item_2 in menu:
            order_total += menu[item_2]

            print(f"{item_2}has been added to order")
        else:
                print("ordered item {item_2} is not avaialablepast!")

        
                print(f"The total amount of items to pay is {order_total}")
