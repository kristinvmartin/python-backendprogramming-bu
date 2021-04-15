"""
Kristin Martin
CS 521
March 10, 2019
Term Project Submission

This file is the class template for a Sunday School class and is used by
BeginSunday.py to instantiate Sunday School class objects.
"""
from datetime import date

class SundaySchoolClass:
    """constructor"""
    
    #static
    categories = ('Nursery','Preschool','Grade School','Teenagers')
    
    #static
    age_groups = {categories[0]:set(range(3)),
                  categories[1]:set(range(3,6)),
                  categories[2]:set(range(6,13)),
                  categories[3]:set(range(13,19))}
    
    def __init__(self,date = str(date.today()),class_type = 'TBA',
                teacher = 'TBA'):
        self.__date = date
        self.teacher = teacher
        self.class_type = class_type
        
    def get_date(self):
        return self.__date
    
    def set_date(self,date):
        self.__date = date
        
    def get_teacher(self):
        return self.teacher
    
    def set_teacher(self,teacher):
        self.teacher = teacher            
        
    def __str__(self):
        return "{} class on {} is being taught by {}".\
                format(self.class_type,self.__date,self.teacher)
        