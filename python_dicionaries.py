#1. Real-World Python Dictionary Applications
#Task 1 Restaurant Menu Update

restaurant_menu = {
    "Starters": {"Soup": 5.99, "Bruschetta": 6.50},
    "Main Course": {"Steak": 15.99, "Salmon": 13.99},
    "Desserts": {"Cake": 4.99, "Ice Cream": 3.99}
}

restaurant_menu["Beverages"] = {"Coffee": 2.50, "Tea": 2.00}

restaurant_menu["Main Course"]["Steak"] = 17.99

del restaurant_menu["Starters"]["Bruschetta"]

for category, items in restaurant_menu.items():
    print(f"{category}:")
    for item, price in items.items():
        print(f"  {item}: ${price:.2f}")

#2. Advanced Data Handling with Python
#Task 1: Hotel Room Booking Tracker

hotel_rooms = {
    "101": {"status": "available", "customer": ""},
    "102": {"status": "booked", "customer": "John Doe"}
}

def book_room(room_number, customer_name):
    """Book a room by marking it as booked and assigning a customer."""
    if room_number in hotel_rooms:
        if hotel_rooms[room_number]["status"] == "available":
            hotel_rooms[room_number]["status"] = "booked"
            hotel_rooms[room_number]["customer"] = customer_name
            print(f"Room {room_number} booked for {customer_name}.")
        else:
            print(f"Room {room_number} is already booked.")
    else:
        print(f"Room {room_number} does not exist.")

def check_out(room_number):
    """Check out a customer by marking the room as available."""
    if room_number in hotel_rooms:
        if hotel_rooms[room_number]["status"] == "booked":
            customer_name = hotel_rooms[room_number]["customer"]
            hotel_rooms[room_number]["status"] = "available"
            hotel_rooms[room_number]["customer"] = ""
            print(f"{customer_name} checked out from Room {room_number}.")
        else:
            print(f"Room {room_number} is already available.")
    else:
        print(f"Room {room_number} does not exist.")

def display_room_statuses():
    """Display the status of all rooms."""
    print("Room Statuses:")
    for room_number, details in hotel_rooms.items():
        print(f"Room {room_number}: {details['status']} ({details['customer']})")


#3. Python Programming Challenges for Customer Service Data Handling
#Task 1: Customer Service Ticket Tracker

service_tickets = {
    "Ticket001": {"Customer": "Alice", "Issue": "Login problem", "Status": "open"},
    "Ticket002": {"Customer": "Bob", "Issue": "Payment issue", "Status": "closed"}
}

def open_ticket(ticket_id, customer_name, issue_description):
    if ticket_id not in service_tickets:
        service_tickets[ticket_id] = {"Customer": customer_name, "Issue": issue_description, "Status": "open"}
        print(f"New ticket {ticket_id} opened for {customer_name}.")
    else:
        print(f"Ticket {ticket_id} already exists.")
        def update_ticket_status(ticket_id, new_status):
    if ticket_id in service_tickets:
        service_tickets[ticket_id]["Status"] = new_status
        print(f"Ticket {ticket_id} status updated to {new_status}.")
    else:
        print(f"Ticket {ticket_id} does not exist.")

def display_tickets(filter_status=None):
    print("Service Tickets:")
    for ticket_id, details in service_tickets.items():
        if filter_status is None or details["Status"] == filter_status:
            print(f"{ticket_id}: {details['Customer']} - {details['Issue']}({details['Status']})")

open_ticket("Ticket003", "Carol", "Network connectivity issue")
update_ticket_status("Ticket001", "closed")
display_tickets(filter_status="open")

#4. Python Essentials for Business Analytics
#Task 1: Sales Data Cloning and Modification
import copy

weekly_sales = {
    "Week 1": {"Electronics": 12000, "Clothing": 5000, "Groceries": 7000},
    "Week 2": {"Electronics": 15000, "Clothing": 6000, "Groceries": 8000}
}

copied_sales = copy.deepcopy(weekly_sales)

copied_sales["Week 2"]["Electronics"] = 18000

print("Original weekly_sales:")
print(weekly_sales)
print("\nCopied and modified weekly_sales:")
print(copied_sales)

