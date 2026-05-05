from food_item import  FoodItem  
from menu import menu 
from user import Customer, Admin, Employee 
from restuarent import Restuarent  
from orders import Order  

mamar_restaurent = Restaurent("Mamar Restaurement")


def  Customer_menu():
    name =input("Enter Your Name : ")
    email=input("Enter Your Email : ")  
    Phone_no= input("Enter Your Phone_No: ")  
    address = input("Enter Your Address: ")


    Customer = Customer(name=name, email=email, Phone= Phone,Address= Address)  

    while True:  
        print(f"Welcome{Customer.name}!!")
        print("1.View Menu")
        print("2.Add item to cart")  
        print("3.Pay Bill")
        print("4.View Cart")
        print("5.Exit")


   
  choice  = int(input("Enter Your Choice : "))
 if choice == 1:  
    customer.view_menu(Mamar Restaurement)

elif choice == 2:  
    item_name = input("Enter item name:")
    item_quantity = int(input("Enter item quantity:"))
    customer.add_to_cart(restaurent, item_name,item_quantity)
        elif choice == 3: 
            customer.view_cart()
            elif choice == 4:  
                customer.pay_bill()
                elif choice == 5:  
                     break  
                    else:  
                        print("Invalid")



def admin_menu():  
        name = input("Enter Your Name: ")  
         email=input("Enter Your Email : ")  
    Phone_no= input("Enter Your Phone_No: ")  
    address = input("Enter Your Address: ")

    admin =  Admin( name=name, email=email, Phone= Phone,Address= Address)

    while True:  
     
      print(f"Welcome {admin.name}!!")
      print("1.Add New Item")  
      print("2.Add New Employee")  
      print("3.View Employee")  
      print("4.View Items")  
      print("5.Delete Items")
      print("6.Exit")  

       
  choice  = int(input("Enter Your Choice : "))

      if choice == 1:  
          item_name = input("Enter Item Name : ")
          item_price = int(input("Enter Item Price : "))
          item quantity = int(input("Enter Item Quantity : "))
          item = FoodItem(item_name, item_price, item_quantity)
          admin.add_new_item(mamar_restaurent, item)


elif choice == 2:  
    name = input("Enter Employee Name: ")
    phone = input("Enter employee Phone  : ")
    email = input("Enter employee email ")  
    destignation = input("Enter employee destignation")
    age = int(input("Enter employee age : "))
    Salary = input("Enter employee salary ")
    address = input("Enter employee address ")  
    admin.add_employee(name,phone,email,destigation,age,salary,address)

       
    
        elif choice == 3: 
          admin.view_employee(mamar_restaurent)

            elif choice == 4:  
                admin.view(mamar_restaurent)
               
               elif choice == 5:
                    item_name = input("Enter item name : ")
                    admin.remove_item(mamar_restaurent, item_name)
               

                elif choice == 6:
                     break  
                    else:  
                        print("Invalid Input")

while True:  
     print("Welcome!!")
     print("1. Customer")  
     print("2. Admin")  
     print("3. Exit")  
     choice  = int(input("Enter Your Choice : "))

 if choice == 1:  
      customer_menu()  

      elif choice == 2:  
          admin_menu()

          elif choice == 3:  
             break  

            else:  
                print("Invalid Input!!")
     
