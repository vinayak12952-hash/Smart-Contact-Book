# 📒 Smart Contact Book (JSON Based)

It is like a digital diary that store data such as name and contact number.
A digital contact directory built using Python. This project moves away from basic text files and uses **JSON** to store and manage user data efficiently in a dictionary format.

## ✨ Key Features
* **Add Contacts:** Safely adds new names and phone numbers to the database.
* **Smart Search:** Instantly searches and retrieves a contact's phone number using their name.
* **Persistent Storage:** Uses JSON (`json.dump` and `json.load`) to ensure data is saved permanently even after the program closes.
* **Object-Oriented Design:** Built using Python Classes and Objects (OOPs) for clean and reusable code.
* **File Handling:** Automatically creates a new `.json` file for new users without crashing.

## 🚀 How It Works
1. The program asks for the user's name to open their specific contact book.
2. If the user is new, it creates a fresh JSON file for them.
3. Users can add a new contact or search for an existing one.
4. The data is updated intelligently without overwriting the entire file history.
