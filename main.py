"Kaixiang Liu"
"9/13/2023"
"Main function for the contact "
import contacts

def main():    
    contact_len = 0
    while True:
        print("***Tuffy Titan Contact Menu")
        print("1. Print list")
        print("2. Add contact") 
        print("3. Modify contact")
        print("4. Delete contact")
        
        print("5. Sort list by first name")
        print("6. Sort list by last name")
        print("7. Exit the program")
        
        userChoice = input("Please enter your selection: ")

        userInp = int(userChoice)

        if userInp == 1:
            contacts.print_list()
        elif userInp == 2:
            firstname = input("please enter the first name: ")
            lastname = input("please enter the last name: ")
            contacts.add_contact(firstname,lastname)
            contact_len += 1
        elif userInp == 3:
            indexNum = int(input("Please enter the index number: "))
            newFirst = input("Please enter the first name: ")
            newLast = input("Please enter the new last name: ")
            contacts.modify_contact(indexNum,newFirst,newLast)
        elif userInp == 4:
            print("Current contact list: ")
            contacts.print_contact()
            indexNum = int(input("please enter the index number: "))
            contacts.delete_contact(indexNum)
            if(contacts.delete_contact(indexNum)):
                contact_len -= 1
        elif userInp == 5:
            if(contact_len <= 0): 
                print("invalid")
            contacts.sort_contact(0)
        elif userInp == 6:
            contacts.sort_contact(1)
            if(contact_len <= 0):
                print("invalid")
        else:
            print("invalid")

if __name__ == "__main__":
    main()