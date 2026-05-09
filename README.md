# Resuarant-Management-System-
A Restaurant Management System (RMS) is a software application designed to automate and manage the daily operations of a restaurant efficiently. It helps in handling tasks such as menu management, order processing, customer handling, and billing.

The system allows users (customers or staff) to view the menu, select food items, and place orders. Each order is recorded and processed, ensuring accurate billing and faster service. The restaurant can manage its menu dynamically by adding, updating, or removing food items.

Additionally, the system maintains user information, tracks orders, and improves coordination between different sections like kitchen and service staff. Overall, it reduces manual work, minimizes errors, and enhances customer satisfaction.


<img width="1536" height="1024" alt="image" src="https://github.com/user-attachments/assets/f51da939-e455-4f5c-9e0e-10a9051b86d3" />


Strong Entities

Strong entities have their own primary key and can exist independently.
class Customer:
    def __init__(self, customer_id, name, phone):
        self.customer_id = customer_id
        self.name = name
        self.phone = phone

        Attributes
customer_id (Primary Key)
name
phone



2. Restaurant (Strong Entity)
class Restaurant:
    def __init__(self, restaurant_id, name, location):
        self.restaurant_id = restaurant_id
        self.name = name
        self.location = location
Attributes
restaurant_id (Primary Key)
name
location



 Employee (Strong Entity)
class Employee:    def __init__(self, employee_id, name, role):        self.employee_id = employee_id        self.name = name        self.role = role
Attributes


employee_id (Primary Key)


name


role



4. FoodItem (Strong Entity)
class FoodItem:    def __init__(self, food_id, name, price):        self.food_id = food_id        self.name = name        self.price = price
Attributes


food_id (Primary Key)


name


price



Weak Entities
Weak entities depend on strong entities for their existence.

5. OrderItem (Weak Entity)
Depends on Order
class OrderItem:    def __init__(self, order_id, food_id, quantity):        self.order_id = order_id        self.food_id = food_id        self.quantity = quantity
Attributes


order_id (Foreign Key)


food_id (Foreign Key)


quantity


Why Weak?


Cannot exist without an Order


Uses foreign keys from other entities



6. Payment (Weak Entity)
Depends on Order
class Payment:    def __init__(self, payment_id, order_id, amount):        self.payment_id = payment_id        self.order_id = order_id        self.amount = amount
Attributes


payment_id


order_id (Foreign Key)


amount


Why Weak?


Payment only exists for a specific order



7. Reservation (Weak Entity)
Depends on Customer
class Reservation:    def __init__(self, reservation_id, customer_id, table_no):        self.reservation_id = reservation_id        self.customer_id = customer_id        self.table_no = table_no
Attributes


reservation_id


customer_id (Foreign Key)


table_no


Why Weak?


Reservation cannot exist without a customer



8. Review (Weak Entity)
Depends on Customer
class Review:    def __init__(self, review_id, customer_id, rating, comment):        self.review_id = review_id        self.customer_id = customer_id        self.rating = rating        self.comment = comment
Attributes


review_id


customer_id (Foreign Key)


rating


comment


Why Weak?


Reviews are written by customers



Simple Explanation
TypeMeaningStrong EntityCan exist independentlyWeak EntityDepends on another entity

Example Relationship
Customer ------ places ------> OrderOrder -------- contains -----> OrderItemOrder -------- has ----------> PaymentCustomer ----- writes -------> Review

Strong & Weak Entity List for ER Diagram
Strong Entities


Customer


Restaurant


Employee


FoodItem


Menu


Supplier


Weak Entities


OrderItem


Payment


Reservation


Review


Bill


Delivery

