import unittest
from contact import Contact
import pyperclip

class TestContact(unittest.TestCase):
    """
    Test class that defines test case for the contact class behaviours
    
    Args:
        unittests.TestCase: helps in creating test cases 
        
    """
    
    def setUp(self):
        """
        Set up method to run before each test case
        
        """
        self.new_contact = Contact("James","Muriuki","0712345678","test@user.com")
        
    def test_init(self):
        """
        test_init test case to test if the object is initialized properly
        """
        self.assertEqual(self.new_contact.first_name, "James")
        self.assertEqual(self.new_contact.last_name, "Muriuki")
        self.assertEqual(self.new_contact.phone_number, "0712345678")
        self.assertEqual(self.new_contact.email, "test@user.com")
        
# if __name__ == "__main__":
#     unittest.main()
    
    
    def test_save_contact(self):
        """
        test if the object contact is being save into the contact list
        
        """
        self.new_contact.save_contact()
        self.assertEqual(len(Contact.contact_list), 1)
        
    def tearDown(self):
        """
        does cleanup after each test case has run 
        """

        Contact.contact_list = []
        
        
    def test_save_multiple_contact(self):
        """
        to check if we can save multiple contact object to our contact list
        """
        self.new_contact.save_contact()
        test_contact = Contact("Test","user","071234578","test@user.com")
        test_contact.save_contact()
        self.assertEqual(len(Contact.contact_list), 2)
        
    def test_delete_contact(self):
        """
        test if we can remove a contact
        """        
        self.new_contact.save_contact()
        test_contact = Contact("Test","user","071234578","test@user.com")
        test_contact.save_contact()
        
        self.new_contact.delete_contact()
        self.assertEqual(len(Contact.contact_list),1)
        
    def test_find_contact_by_number(self):
        """
        find a contact by phone number and display it 
        """
        
        self.new_contact.save_contact()
        test_contact = Contact("Test","user","0712345678","test@user.com")
        test_contact.save_contact()
        
        found_contact = Contact.find_by_number("0712345678")
        
        self.assertEqual(found_contact.email, test_contact.email)
        
    def test_contact_exists(self):
        """
        test to check if we can return a boolean if we cannot find the contract
        """            
            
        self.new_contact.save_contact()
        test_contact = Contact("Test","user","0712345678","test@user.com")
        test_contact.save_contact()
            
        contact_exists = Contact.contact_exist("0712345678")
            
        self.assertTrue(contact_exists)
        
        
    def test_display_all_contacts(self):
        """
        returns a list of all contacts saved
        """
        self.assertEqual(Contact.display_contacts(), Contact.contact_list)
        
    def test_copy_email(self):
        """
        Test to confirm that we are copying the email address from a found contact
        """        
        self.new_contact.save_contact()
        Contact.copy_email("0712345678")
        
        self.assertEqual(self.new_contact.email, pyperclip.paste())
    
    
        
        
if __name__ == "__main__":
    unittest.main() 
    
        