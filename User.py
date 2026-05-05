# Customer  
# Employee
# Admin  

from abc import ABC
from Orders import Order

class User(ABC):
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

   class Customer(User):
        def __init__(self, name, phone, email, address):
        super().__init__(name, phone, email, address)
         self.cart = Order()

        

         def view_menu(self,restuarent):
                restuarent.menu.show_menu()

                def add_to_cart(self,restuarent,item_name):
                    item  =  restuarent.menu.find_item(item_name)
                    print(item.name)
                    if item:
                             
                           if quantity > item.quantity:
                                print("Item quantity exceeded!!")
    
                       else:
                         item.quantity = quantity
                         self.cart.add_item(item)
                         print("Item Added")
                    else:  
                        print("Item not found")    
          
           def view_cart(self):
           print("**view cart**")
           print("Name\tPrice\tQuantity")
           for item, quantity in self.cart.items.items():
                print(f"{item.name}{item.price}{quantity}")
                
                 print(f"Total Price : {self.cart.total_price()}")



  def pay_bill(self):  
    print(f"Total{self.cart.total_price} paid successfully")
    self.cart.clear()


# class  Order(User):  
#       def _init_(self) -> None:  
#         self.item = []
          
#           def add_item(self,item):
#                 if item in self.items:  
#                     self.items[item] += item.quantity

#               else:  
#                    self.items[item] += item.quantity


#      def remove(self,item):
#             if item in  self.items:
#                 del self.items[item]
                

#          @property 
#        def  total_price(self):
#                  return  sum(item.price * quantity for item, quantity in self.items.items())

#                  def clear(self):
#                         self.items = {}
       

class Employee(User):
    def __init__(self, name, phone, email, address, employee_id, position, salary, age):
        super().__init__(name, phone, email, address)
        self.employee_id = employee_id
        self.position = position
        self.salary = salary
        self.age = age

#emp =  Employee("John Doe", "1234567890", "Employee", "123 Main St", "E001", "Chef", 50000, 30)        
#print(emp.name)  # Output: John Doe        
#print(emp.employee_id)  # Output: E001


class Admin(User):
    def __init__(self, name, phone, email, address):
        super().__init__(name, phone, email, address)
        self.employees = [] #eta hocchge amader database jekhane amra employee der store korbo  
          
          def view_employee(self,restaurant):
                restaurant.view_employee()
    
            def add_new_item(self,restuarant, item):
                restaurant.menu.add_item(item)

              def remove_item(self, restuarant, item_name):     
                restaurant.menu.remove_item(item_name)  

                

    def add_employee(self, name, phone, email, address, employee_id, position, salary, age):
        #Emplyee Class e arekta object create korbo and tarpor oi object ke amader employee list e add kore dibo                
        employee = Employee(name, phone, email, address, employee_id, position, salary, age)
        self.employees.append(employee)
        print(f"Employee {employee.name} added successfully.")

    def view_employee(self):
        print("Employee List:")      
        for employee in self.employees:
            print(f"Name: {employee.name}, Position: {employee.position}, Salary: {employee.salary}")

      def add_new_item(self,restaurent,item):  
           restaurent.add_new_item(item)

           def remove_item(self,restaurent,item): 
               restaurent.remove_item(item)  

        def view_menu(self,restaurent,item):  
               restaurent.view_menu(item)
     

# class Restaurant:
#     def __init__(self, name, location):
#         self.name = name        
#         self.location = location
#         self.menu = FoodItem()

    
#     def add_employee(self,restaurant, employee): 
#         restaurant.employees.append(employee)


#       def view_employee(self,restuarant):
#              print("Employee List:")
#              for emp in self.employees:
#                 print(emp.name, emp.position, emp.salary)
            
            
#              restauarant.view_employee()    

#         def  add_new_item(self,restuarant, item):
#             restuarant.menu.add_item(item)     

        


# class Menu:
#     def __init__(self):
#         self.items = []
    
#     def add_item(self, name, price):
#         item = {"name": name, "price": price}
#         self.items.append(item)
    
#     def find_items(self, item_name):
#         for item in self.items:  
#             if item["name"].lower() == item_name.lower():        
#                 return item     
#         return None 

#     def remove_item(self, item_name):
#         for item in self.items: 
#             if item["name"].lower() == item_name.lower():        
#                 self.items.remove(item)        
#                 print(f"Item {item_name} removed successfully.")
#                 return
#         print(f"Item {item_name} not found in the menu.")


#          class FoodItem:  
#                 def _init_(self, name, price, quantity)
#                  self.name = name  
#                  self.price = price  
#                  self.quantity = quantity  

   
#                 ad = Admin("Admin", "123123", "admin@example.com", "456 Admin St")      

#                 ad.add_employee("Sagor", "9876543210", "sagor@example.com", "789 Employee St", "E002", "Waiter", 40000, 25)    
#                  mamar_res = Restuarent("Mamar Restuarent")
#                  mn = menu()
#                  item  = FoodItem("Pizza",12.45,10)
#                  item2 = FoodItem("Burger",10,30)
#                  admin = Admin("Rahim","Rahim@gmail.com",123123,"Dhaka")
#                  admin.,add_new_item(item)
#                  mn.add_menu_item(item)
#                  mn.show_menu()                
#                 ad.view_employee()


#         customer1 = Customer("Rahim","Rahim@gmail.com",121123,"Dhaka")
#         customer1.view_menu(mamar_res)



#         item_name =input("Enter item Name: ")
#         item_quantity = int(input("Enter Item Quantity : "))
