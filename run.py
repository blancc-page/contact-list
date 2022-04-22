#! /usr/bin/python

from contact import Contact
import pyperclip

def create_contact(fname,lname,phone,email):
    """fuction to crate new contact

    Args:
        fname (str): first name
        lname (str): last name
        phone (str): phone number
        email (str): email address
    """    
    new_contact = Contact(fname,lname,phone,email)
    return new_contact

def save_contacts(contact):
    """save contact

    Args:
        contact (Contact): Contact class
    """    
    contact.save_contact()
    
def del_contact(contact):
    """deletes a contact

    Args:
        contact (class): Contact class
    """    
    Contact.delete_contact(contact)
    print(f"{contact} deleted.")
    
def check_existing_contacts(number):
    """checks if number exists

    Args:
        number (str)): phone number
    """    
    return Contact.contact_exist(number)
    
def display_contacts():
    """
    Function that returns all the saved contacts
    """    
    return Contact.display_contacts()

def find_number(number):
    """searches for number

    Args:
        number (str): phone number
    """
    
    return Contact.find_by_number(number)

def cpy_email(contact):
    """copies email to clipboard

    Args:
        email (str): email address
    """
    
    Contact.copy_email(contact)


def main():
    print("Hello Welcome to your contact list. What is your name?")
    user_name = input()

    print(f"Hello {user_name}. what would you like to do?")
    print('\n')

    while True:
            print("Use these short codes : cc - create a new contact, dc - display contacts, fc -find a contact, delc- delete a contact, cpyc- copy a contact, ex -exit the contact list ")

            short_code = input().lower()

            if short_code == 'cc':
                    print("New Contact")
                    print("-"*10)

                    print ("First name ....")
                    f_name = input()

                    print("Last name ...")
                    l_name = input()

                    print("Phone number ...")
                    p_number = input()

                    print("Email address ...")
                    e_address = input()


                    save_contacts(create_contact(f_name,l_name,p_number,e_address)) # create and save new contact.
                    print ('\n')
                    print(f"New Contact {f_name} {l_name} created")
                    print ('\n')

            elif short_code == 'dc':

                    if display_contacts():
                            print("Here is a list of all your contacts")
                            print('\n')

                            for contact in display_contacts():
                                    print(f"{contact.first_name} {contact.last_name} .....{contact.phone_number}")

                            print('\n')
                    else:
                            print('\n')
                            print("You dont seem to have any contacts saved yet")
                            print('\n')

            elif short_code == 'fc':

                    print("Enter the number you want to search for")

                    search_number = input()
                    if check_existing_contacts(search_number):
                            search_contact = find_number(search_number)
                            print(f"{search_contact.first_name} {search_contact.last_name}")
                            print('-' * 20)

                            print(f"Phone number.......{search_contact.phone_number}")
                            print(f"Email address.......{search_contact.email}")
                    else:
                            print("That contact does not exist")

            elif short_code == "ex":
                    print("Bye .......")
                    break
                
            elif short_code == "delc":
                print("Enter the contact you wish to delete:")
                search_number = input()
                if check_existing_contacts(search_number):
                    search_contact = find_number(search_number)
                    print(f"Are you sure you want to delete {search_contact.first_name} {search_contact.last_name}'s contact? Y for Yes and N for No.")
                    answer = input()
                    if answer == "Y":
                        del_contact(search_contact)
                        print(f"{search_contact}'s contact is deleted.")
                    elif answer == "N":
                        print("Not Deleted")
                    else:
                        print("Invalid Option")
            elif short_code == "cpyc":
                 print("Enter the number of the contact whose email you wish to copy:")
                 search_number = input()
                 if check_existing_contacts(search_number):
                    search_contact = find_number(search_number)
                    print(f"Would you like to copy {search_contact.first_name}'s email? Y for Yes and N for No.")
                    answer = input()
                    if answer == "Y":
                        cpy_email(search_contact.email)
                        print(f"{search_contact}'s email is copied.")
                    elif answer == "N":
                        print("Not Copied")
                    else:
                        print("Invalid Option")
 
            else:
                    print("I really didn't get that. Please use the short codes")
                            
if __name__ == '__main__':

    main()