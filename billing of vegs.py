def print_table():
    print("-------------------------------------------")
    print("no".ljust(3, ' '), "fruit".ljust(8, ' '), "rate".ljust(4, ' '), "quan".ljust(4, ' '))
    print("-------------------------------------------")
    for i, j in fruits.items():
        print(str(i).ljust(3, ' '), j[0].ljust(8, ' '), str(j[1]).ljust(4, ' '), str(j[2]).ljust(4, ' '))



print("                             ********************** WELCOME ***********************")
print("                                    First Check Below Fruits List With Price          ")
print("                                        Then Order Your Favorite Fruits!              ")
print("                             ******************************************************")
print("                                                       ")
fruits = {1: ['mango', 70, 20],
          2: ['apple', 120, 30],
          3: ['cherry', 150, 70],
          4: ['papaya', 90, 60],
          5: ['grapes', 130, 55],
          6: ['orange', 200, 90]}
#ans=0
Total=0
#f=0
while(1):
    print_table()
    print("------------------------------------------")
    print("If You Want To Exit Please Enter 0 ")
    print("------------------------------------------")
    fruits_no = int(input("enter your fruits number: "))
    if fruits_no==0:
        print("**************************************")
        print("Your Total Bill: ", Total)
        print("THANK YOU VISIT AGAIN!")
        print("**************************************")
        break
    else:
        if fruits_no in fruits.keys():
            print("available quantity for",fruits[fruits_no][0],"is",fruits[fruits_no][2],"kg Please enter quantity less than",fruits[fruits_no][2],"kg")
            quantity = int(input("enter your fruits quantity-per kg : "))
            if quantity<fruits[fruits_no][2]:
                print("*************************************************")
                print("your bill for", fruits[fruits_no][0], "with quantity", quantity,"kg is",quantity*fruits[fruits_no][1],"rupees")
                fruits[fruits_no][2]=fruits[fruits_no][2]-quantity
            else:
                print("available quantity is", fruits[fruits_no][2], "kg Please enter quantity less than",
                      fruits[fruits_no][2], "kg")
            Total = Total + quantity * fruits[fruits_no][1]
            print("your Total bill now is", Total,"rupees.")
            print("*************************************************")# comment
        else:
            print("              sorry, Please enter a valid number!")
            print("              choose a  number from below fruits list ")#print comment
            continue







