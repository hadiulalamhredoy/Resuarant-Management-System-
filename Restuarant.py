class Restaurant:
    def __init__(self, name, location):
        self.name = name        
        self.location = location
        self.menu = FoodItem()

    
    def add_employee(self,restaurant, employee): 
        restaurant.employees.append(employee)


      def view_employee(self,restuarant):
             print("Employee List:")
             for emp in self.employees:
                print(emp.name, emp.position, emp.salary)
            
            
             restauarant.view_employee()    

        def  add_new_item(self,restuarant, item):
            restuarant.menu.add_item(item)     

        