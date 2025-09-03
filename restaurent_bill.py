import datetime

tym = datetime.datetime.now()

# takes menu from txt file
menu = {}
with open("D:/Luminar/Python/Project/menu.txt", "r") as f :
    for line in f :
        parts = line.strip().split()
        if len(parts) == 3 :
            code, name, price = parts
            menu[code] = (name.replace("_", " "), int(price))

#  printing menu
print(" " * 10,"Menu")
print("-" * 26)
for code, (name, price) in menu.items():
    print(f"{code:<4} {name:<16} ₹{price}")
print("-" * 26)

#  getting table number

tables = 20
table_num = input("Enter table number (1-20) : ")
while not (table_num.isdigit() == True and (0 < int(table_num) <= tables))  :
    table_num = input("Enter a valid table number (1-20) : ")

#  getting ordered foods in a list

food = []
order = []

for i in menu :
    food.append(i)

ans = ""
while ans == "" or ans == "y":

    food_items = input("Enter ordered food items (code) : ")
    while food_items not in food :
        food_items = input("Enter a valid food code : ")
        
    qty = int(input("Enter quantity : "))
    while qty < 1 :
        qty = int(input("Enter a valid quantity : "))
    
    order.append({food_items : qty})
            
    ans = input("Add more (y/n) : ").lower()
            
    if ans == " " or ans == "n" :
        break

#  getting customer name & checks if entered a valid name

customer_name = input("Enter customer name : ")
while customer_name.isalpha() == False :
    for i in customer_name :
        if i == " " :
            continue
        elif i.isalpha() != True :
            customer_name = input("Enter a valid name : ")    
    break

#  getting phone number from customer & checks if entered a valid number

ph_num = input(f"Enter {customer_name}'s phone number : ")
while len(str(ph_num)) != 10 or int(ph_num.isdigit()) == False or ph_num.isalpha() == True :
    ph_num = input("Enter a valid phone number : ")

#  generating bill

print("\nGenerating bill!!...\n")

sub_total = 0
bill = []

bill.append("=" * 44 + "\n")
bill.append(" " * 15 + "ABC RESTAURENT")
bill.append(" " * 15 + "-" * 14 + "\n")
bill.append(f"Date: {tym.strftime('%d-%m-%Y')}" + " " * 10 + f" Time: {tym.strftime('%I-%M-%S %p')}" + "\n")
bill.append(f"Table number: {table_num}")
bill.append(f"Customer name: {customer_name}")
bill.append(f"Phone: {ph_num}" + "\n")
bill.append(f"{'Items' :<20} {'Price' :<8} {'Qty' :<8} {'Total'}")
bill.append("-" * 44)

for i in order :
    for code, qty in i.items() :

        name, price = menu[code]
        total = price * qty
        sub_total += total

        bill.append(f"{name:<22} {price :<7} {qty :<8} {total}")

gst = round(sub_total * 0.05, 2)
serv_tax = round(sub_total * 0.1, 2)
grand_total = round(sub_total + gst + serv_tax, 2)

bill.append("-" * 44)
bill.append(" " * 33 + f"Total: {sub_total}")
bill.append("-" * 44)
bill.append(f"GST" + f"{':':>10} {gst}")
bill.append(f"Service Tax : {serv_tax}")
bill.append("-" * 44)
bill.append(f"Grand Total : {grand_total}")
bill.append("-" * 44)
bill.append("\n" + " " * 12 + "...!!THANK YOU!!..." + "\n")
bill.append("=" * 44)

print("\n".join(bill))

#  saving as a txt file

file = f"D:/Luminar/Python/Project/receipt/{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}_{customer_name.lower()}.txt"
with open(file,"w") as f :
    f.write("\n".join(bill))

