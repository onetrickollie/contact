"Kaixiang Liu"
"9/13/2023"
#a contact list that can do the following:
#1. add names to the contact list
#2. modify contact if necessary
#3. delete contact
#4. view the entire contact list
#5. sort list by alphabetical order
contact = []

def print_contact():
    print(contact)

def print_list():
    print(" ================== CONTACT LIST ==================")
    print("Index   First Name            Last Name")
    print("======  ====================  ====================")
    counter = 0
    for i in range(len(contact)):
        print(counter,"       ",contact[counter][0],"               ",contact[counter][1])
        counter=counter+1
    
#def add_contact(new_contact):
    #contact.append(new_contact)
    #return contact

def add_contact(new_contact, **kwargs):
    first_name = kwargs.get('first_name', '')
    last_name = kwargs.get('last_name', '')

    if first_name and last_name:
        new_contact = [first_name, last_name]

    contact.append(new_contact)
    return contact

def modify_contact(index,newFirst,newLast):
    if index < 0 or index>len(contact)-1:
        print("Invalid index number. ")
    else:
        contact[index] = [newFirst,newLast]
    return contact
def delete_contact(index):
    if(index < 0 or index > len(contact)-1):
        print("Invalid index number")
        return contact
    else:
        del contact[index]
    return contact
def sort_contact(col):
    global contact
    if col == 0:
        contact = sorted(contact, key=lambda x: x[0])
    elif col == 1:
        contact = sorted(contact, key=lambda x: x[1])

    
    

