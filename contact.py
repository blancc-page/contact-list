# import numbers


# class Contact:
#     """
#     Class that generates new instances of contacts
    
#     """
    
#     conatct_list = []
    
#     def __init__(self, first_name, last_name, phone_number, email):

#         """
#         __init__ method that helps us define properties for out objects

#         Args:
#             first_name: New first name
#             last_name: new last name
#             number: new phone number
#             email: new email address
            
#         """
    
#         self.first_name = first_name
#         self.last_name = last_name
#         self.phone_number = phone_number
#         self.email  = email
        
    # pass
import pyperclip

class Contact:
    """
    Class that generates new instances of contacts.
    """
    contact_list = []
    
    def save_contact(self):
        """
        save_contact methos saves contactobject into contact_list
        
        """
        Contact.contact_list.append(self)
        
    def delete_contact(self):
        """
        delets a saved contact
        """
        Contact.contact_list.remove(self)
        
    @classmethod
    def find_by_number(cls,number):
        """takes it a number and returns a contact that matches it

        Args:
            number (number): phone number
        """        
        
        for contact in cls.contact_list:
            if contact.phone_number == number:
                return contact
    
    @classmethod
    def contact_exist(cls,number):
        """checks if a contact exists

        Args:
            number (number): phone number 
        """        
        for contact in cls.contact_list:
            if contact.phone_number == number:
                return True
        return False
    
    @classmethod
    def display_contacts(cls):
        """
        method that returns the conatact list
        """        
        
        return cls.contact_list
    
    @classmethod
    def copy_email(cls, number):
        contact_found = Contact.find_by_number(number)
        pyperclip.copy(contact_found.email)
    
    def __init__(self,first_name,last_name,number,email):

      # docstring removed for simplicity

        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = number
        self.email = email
        



    

    
