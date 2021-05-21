#%%
import csv

#%%
ContactsList = []

#%%
def show_():
    if len(ContactsList) == 0:
        print("No contacts in list!")
    else:
        print("{0:>3}  {1:<15}  {2:>12}".format("Index","Name","Number"))
        index = 0
        for contact in ContactsList:
            index = index + 1
            print("{0:>5}  {1:<19}  {2:>12}".format(index, contact[0], contact[1]))

#%%
def new_():
    name = input("Enter a name: ")
    number = input("Enter a number: ")
    if name == "":
        name = "No name"
    if number == "":
        number = "No number"
    ContactsList.append([name.capitalize(),number.capitalize()])
    print("The name is: ",name.capitalize())
    print("The number is: ",number.capitalize())
    print("Contact added to contacts list.")
    while True:
        recreate = input("Would you like to create another contact? : ")
        if recreate.lower() == "yes":
            name = input("Enter a name: ")
            number = input("Enter a number: ")
            ContactsList.append([name.capitalize(),number.capitalize()])
            print("The name is: ",name.capitalize())
            print("The number is: ",number.capitalize())
            print("Contact added to contacts list.")
        elif recreate.lower() == "no":
            break
        else:
            print("Invalid choice!")
            break
#%%
def edit_():
    which = input("Which contact would you like to edit? : ")
    if which == "":
        print("You have not entered anything.")
        return
    if not which.isdigit():
        print ("'", which, "' needs to be the index number of a contact!")
        return
    which = int(which)
    if which < 1 or which > len(ContactsList):
        print("'", which, "' is not in range of index numbers")
        return
    
    contact = ContactsList[which-1]
    print("The current name is: ",contact[0])
    print("The current number is: ",contact[1])
    newname = input("Enter a new name for this contact or press <enter> to leave unchanged: ")
    if newname == "":
        newname = contact[0]
    newnumber = input("Enter a new number for this contact or press <enter> to leave unchanged: ")
    if newnumber == "":
        newnumber = contact[1]
    contact = [newname,newnumber]
    print("The new name is: ",contact[0])
    print("The new number is: ",contact[1])
    ContactsList[which-1] = contact
    
#%%
def delete_():
    which = input("Which contact would you like to delete? : ")
    if which == "":
        print("You have not entered anything.")
        return
    if not which.isdigit():
        print ("'", which, "' needs to be the index number of a contact!")
        return
    which = int(which)
    if which < 1 or which > len(ContactsList):
        print("'", which, "' is not in range of index numbers")
        return
    
    clarification = input("Are you sure you would like to delete this contact: ")
    if clarification.lower() == "yes":
        del ContactsList[which-1]
        print("This contact has been deleted.")
    elif clarification.lower() == "no":
        print("This contact has not been deleted.")
    else:
        print("Invalid option! This contact will not be deleted.")

#%%
while True:
    print("Choose one of the following options?")
    print("Show")
    print("Create")
    print("Delete")
    print("Edit")
    print("Quit")
    choice = input("Choice: ")
    
    if choice == "":
        continue
    elif choice.lower() == "show":
        show_()
        print()
    elif choice.lower() == "create":
        new_()
        print()
    elif choice.lower() == "delete":
        delete_()
        print()
    elif choice.lower() == "edit":
        edit_()
        print()
    elif choice.lower() == "quit":
        ContactsList.sort()
        save = input("Would you like to save your contacts? : ")
        if save.lower() == "yes":
            f = open("Contacts.csv", 'w', newline='')
            for item in ContactsList:
                csv.writer(f).writerow(item)
            f.close()
            print("Exited and saved. Thank you!")
            break
        elif save.lower() == "no":
            print("Exited. Thank you!")
            break
        else:
            print("Invalid choice!")
            print()
    else:
        print("Invalid choice!")
        print()

#%%
