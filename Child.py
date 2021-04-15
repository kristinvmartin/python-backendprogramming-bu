"""
Kristin Martin
CS 521
March 10, 2019
Term Project Submission

This file is the class template for a Child object and is used by
BeginSunday.py to instantiate Child objects representing students in a 
Sunday School class.
"""
from Validation import Validation

class Child:
    def __init__(self,first_name,last_name,age,guardian_first_name,
                 SMS_contact,is_checked_in = False):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__age = age
        self.__guardian_first_name = guardian_first_name
        self.__SMS_contact = SMS_contact
        self.is_checked_in = is_checked_in
        
    def get_first_name(self):
        return self.__first_name
    
    def set_first_name(self,first_name):
        self.__first_name = first_name
        
    def get_last_name(self):
        return self.__last_name
    
    def set_last_name(self,last_name):    
        self.__last_name = last_name

    def get_age(self):
        return self.__age
    
    def set_age(self,age):
        self.__age = age
    
    def get_guardian_first_name(self):
        return self.__guardian_first_name
    
    def set_guardian_first_name(self,guardian_first_name):
        self.__guardian_first_name = guardian_first_name
    
    def get_SMS_contact(self):
        return self.__SMS_contact
    
    def set_SMS_contact(self,SMS_contact):
        self.__SMS_contact = SMS_contact
        
    def get_is_checked_in(self):
        return self.is_checked_in
    
    def set_is_checked_in(self,is_checked_in):
        self.is_checked_in = is_checked_in
        
    def __str__(self):
        return "Child: {} {}, Age {}. Guardian: {}. Guardian Phone: {}".\
               format(self.__first_name,self.__last_name,self.__age,\
                      self.__guardian_first_name,self.__SMS_contact) 
        
    def new_from_input(dictionary):
        """
        desc:        creates a new Child object from user input
        input param: the dictionary where the object will be put
        returns:     none, adds child to dictionary and prints confirmation
        """
        
        #user input - validates using methods at top of script
        first_name = Validation.validate_alpha("Enter the child's first name: ").title()
        last_name = Validation.validate_alpha("Enter the child's last name: ").title()
        age = Validation.validate_age("Enter the child's age: ")
        guardian_first_name = Validation.validate_alpha("Enter the guardian's first name: ").title()
        SMS_contact = Validation.validate_phone("Enter the SMS phone number of the guardian: ")
        
        #creates new child instance and puts in dictionary with key
        #that follows established convention
        new_child = first_name.title() + last_name[0].upper()
        dictionary.update({new_child:Child(first_name,last_name,age,
                                         guardian_first_name,SMS_contact)})
        
        #prints confirmation to user
        print("New Child Created.")
        print(dictionary[new_child])
    
    def remove_from_dict(dictionary,key):
        """removes child from existing dictionary"""
        dictionary.pop(key)
        print("Child {} removed from current listing.".format(key))
    