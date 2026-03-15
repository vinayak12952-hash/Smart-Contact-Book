# inporting JSON
import json
# importing OS
import os


# Creating a class i.e. blue for every object.
class ContactBook:
    # Initial method
    def __init__(self, name):
        self.name = name 
        self.file = f"{name}_contacts.json"

        # Check that is the file in the folder or not?
        if os.path.exists(self.file):
            with open (self.file, "r") as file:
                self.info = json.load(file)
                print(self.info)
        else:
            with open (self.file, "w") as file:
                json.dump({},file)

    # Function used to add new data in the file
    def add(self, user_input_name, user_input_no):
        self.user_input_name = user_input_name
        self.user_input_no = user_input_no
        
        with open(self.file, "r")as file:
            self.data =json.load(file)

        self.data[user_input_name] = user_input_no
        
        with open (self.file , "w") as file:
            json.dump(self.data, file, indent = 4)
            print("Data entry successful!")

    # Help in searching of contacts
    @staticmethod
    def search():
        turn = 0
        while True:    
            # Exiting code.
            if turn > 0:
                a = input("Do you want to exit? (yes/no) ").strip().lower()
                if a == "yes":
                    print("Thanks for using!")
                    break
                elif a != "no":
                    print("You need to give answer in yes/no!")
                    continue
            target = input("Enter the name, to find contact-  ").capitalize()
            with open("1_contacts.json", "+r") as f1:
                data = json.load(f1)
                if target in data:
                    print(data[target])
                    turn += 1
                    continue
                else:
                    print("Contact not found!")
                    continue

# Object creation
P1 = ContactBook("1")
P1.add("Ram", "9859879204")
P1.search()

