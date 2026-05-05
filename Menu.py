class Menu:
    def __init__(self):
        self.items = []
    
    def add_item(self, name, price):
        item = {"name": name, "price": price}
        self.items.append(item)
    
    def find_items(self, item_name):
        for item in self.items:  
            if item["name"].lower() == item_name.lower():        
                return item     
        return None 

    def remove_item(self, item_name):
        for item in self.items: 
            if item["name"].lower() == item_name.lower():        
                self.items.remove(item)        
                print(f"Item {item_name} removed successfully.")
                return
        print(f"Item {item_name} not found in the menu.")
