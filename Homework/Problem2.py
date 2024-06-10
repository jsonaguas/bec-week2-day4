import random
service_tickets = {
    1: {"Customer": "Alice", "Issue": "Login problem", "Status": "open"},
    2: {"Customer": "Bob", "Issue": "Payment issue", "Status": "closed"}
    
}

'''
1-Open a new service ticket.
2- Update the status of an existing ticket to "closed".
3- Display all tickets.'''

def next_id():
    last_id = 0
    for id in service_tickets.keys():
        if id > last_id:
            last_id = id
    return last_id + 1

def new_ticket():
    new_id = next_id()
    while True:
        customer = input("Please enter the customer name: \n")
        issue = input ("Please state the issue: \n")
        status = input("What is the status of this ticket? open / closed").lower()
        print(f"Customer: {customer}, Issue: {issue}")
        correct = input("Does this information look correct?")
        if correct == 'y': # create ticket
            service_tickets[new_id] = {"Customer": customer, "Issue": issue, "Status": "open"}
            return
        else:
            continue

def view_tickets():
    # for ticket in range(len(service_tickets)):
    #     print(f"{service_tickets[ticket+1]} ")
    # return service_tickets
    for key,value in service_tickets.items():
        print(key,value)
        
def update_ticket():
    print("Select existing ticket")
    view_tickets()
    while True:
        ticket_number = int(input("Enter number "))
        if ticket_number in service_tickets:
            service_tickets[ticket_number]["Status"]="closed"
            break
        else:
            print("Invalid ticket number. Please try again.")

def main():
    while True:
        ans = input ('''
                     )
SERVICE TICKET MANAGER
1-Open a new service ticket.
2- Update the status of an existing ticket to "closed".
3- Display all tickets.
                     ''')
        
        if ans == '1':
            new_ticket() # function to add a new ticket
        elif ans == '2':
            update_ticket() # function to update an existing ticket
        elif ans == '3':
            view_tickets() # function to display all tickets
        elif ans == '4':
            print("Thanks for making service tickets n stuff like that. Have a good one.")
            break
        else:
            print("Invalid input. Please try again.")
    
main()
