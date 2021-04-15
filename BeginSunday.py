"""
Kristin Martin
CS 521
March 10, 2019
Term Project Submission

This is the main project submission file. Please refer to the README.txt
before running this script.

This script represents any given Sunday morning for a Sunday School teacher
who is automating the process of the administration of Sunday School classes.
"""
from SundaySchoolClass import SundaySchoolClass
from Child import Child
from Validation import Validation

class FileCategoryError(Exception):
    """Raised when text file contains category not in tuple"""
    pass

def sample_setup():
    """sample data: pre-loaded dictionary with children"""
    
    global children
    children = {'XanderM'  : Child('Xander','Martin',4,'Kristin','5083353207'),
                'AriannaM' : Child('Arianna','Martin',6,'Kristin','5083353207'),
                'FaithS'   : Child('Faith','Stone',2,'Tommie','7745689793'),
                'AffinityD': Child('Affinity','Desiderio',17,'Brooke',None),
                'TeddyM'   : Child('Teddy','McCord',1,'Mary Ann','4483082917'),
                'DaVonteT' : Child('DaVonte','Tellier',11,'Brooke','7754974836')}
    
    return children #for testing

class SetupSunday:
    
    def setup_teacher_assignments(file):
        """
        desc:        creates instances of SundaySchoolClass for each category
                     including reading teacher info from a txt file.
        input param: file to be read
        returns:     teacher_assignments dictionary, sunday class instances as list
        """
        global sunday_class_instances
        global teacher_assignments
        #to be loaded each week from setup_teacher_assignments
        sunday_class_instances = []
    
        #to be loaded each week from txt file in setup_teacher_assignments
        teacher_assignments = {}
        
        try:
            teacher_assign_file = open(file,"r")
            #read lines, assign key/val pairs to dict
            for line in teacher_assign_file:
                line = line.rstrip().title()
                (key,val) = line.split(" = ")
                if key not in SundaySchoolClass.categories:
                    raise FileCategoryError
                teacher_assignments[key] = val
            teacher_assign_file.close()
            
            #create instances of SundaySchoolClass
            for i in range(len(SundaySchoolClass.categories)):
                sunday_class_instances.append\
                (SundaySchoolClass(class_type = SundaySchoolClass.categories[i],
                                   teacher = teacher_assignments[SundaySchoolClass.categories[i]]))
                print(sunday_class_instances[i])
            
            return teacher_assignments #for testing
        
        except FileCategoryError:
            print("Your file contains a category that is\
                  \nnot in the established tuple: {}.\
                  \nCorrect the file and try again.".format(SundaySchoolClass.categories))
        
        except FileNotFoundError:
            print("The file you entered was not found.\
                  \nCheck that the file is saved in the current directory and try again.")
    
    def determine_child_classroom(child):
        """
        desc:        called by other methods to determine child's classroom by age
        input param: child - the instance of object child to be assigned
        returns:     the child's classroom
        """
        for i in range(len(SundaySchoolClass.age_groups)):
            if child.get_age() in SundaySchoolClass.age_groups[SundaySchoolClass.categories[i]]:
                return SundaySchoolClass.categories[i]
                break
    
    def child_check_in(child):
        """
        desc:        sets status of child as "checked in" to a given Sunday School
                     class category based on their age, updates historical log for
                     attendance tracking
        input param: child - the instance of object child to be checked in
        returns:     none (prints confirmation of check-in)
        """
        child.set_is_checked_in(True)
        classroom = SetupSunday.determine_child_classroom(child)
       
        print("{} is checked in to {} with {}".format(child.get_first_name(),
              classroom, teacher_assignments[classroom]))
    
    def child_check_out(child):
        """
        desc:        sets status of child as "checked out" from a given Sunday School
                     class category based on their age, updates historical log for
                     attendance tracking
        input param: child - the instance of object child to be checked in
        returns:     none (prints confirmation of check-in)
        """
        if child.get_is_checked_in() is True:
            child.set_is_checked_in(False)
            classroom = SetupSunday.determine_child_classroom(child)
            print("{} is now checked out of {} with {}".\
                  format(child.get_first_name(),classroom,
                         teacher_assignments[classroom]))
        else:
            print("{} was not checked in.".format(child.get_first_name()))
        
    def page_guardian(child):
        """
        desc:        outputs the SMS number and name of guardian for teacher to
                     contact during Sunday School if needed.
        input param: child - corresponding instance of Child object
        returns:     none, prints SMS number and guardian name
        """
    
        print("{}: {} is needed in the {} room.".\
              format(child.get_SMS_contact(),child.get_guardian_first_name(),
                     SetupSunday.determine_child_classroom(child)))
        
    def menu_options(list_,input_message):
        """
        desc:        presents numbered option menu based on input list, returns selection
        input param: list_: list to be presented
        input param: input_message: message to display when prompting for user input
        returns:     list element at corresponding # position
        """
        
        for i in range(len(list_)):
            print(i,list_[i])
        valid_input = False
        while not valid_input:
            try:
                number = int(input(input_message))
                if number not in range(len(list_)):
                    raise ValueError
                else:
                    for i in range(len(list_)):
                        if i == number:
                            item = list_[i]
                            continue
                    valid_input = True
                    return item
        
            except ValueError:
                print("Select a number to match the corresponding child.")
    
def present_menu():
    """
    desc:        initiates the program, presents menu to user, persists until
                 user quits
    input param: none
    returns:     none
    """
    #initiate variables used in method
    ready_to_load = str()
    checked_in_kids = []
    
    print()
    print("Welcome to church!")
    print("Please set up your teacher and classroom assignments before beginning.")
    print("Use Teachers.txt to adjust your teachers for the week.\
          \nDo NOT change the categories. Save the file when done.")
    while ready_to_load != 'go':
            ready_to_load = input("Type 'go' when ready to load:")\
            .lower().strip()
    print()
    print("Great!  Your teacher assignments for today are:")
    print()
    SetupSunday.setup_teacher_assignments("Teachers.txt")

    #present main menu options until user quits
    selection = 0
    while selection != 7:
        
        print()
        print("Welcome to the main menu! Here's what you can do: ")
        print()
        print("1: Check a child into class that's already been here")
        print("2: Check out a child that is in currently in a class")
        print("3: Set up a new child")
        print("4: Remove a child from the current directory of students")
        print("5: Page a parent/guardian")
        print("6: Update parent/guardian information of a previously set up child")
        print("7: Close the Sunday School and check out all children.")
        
        #get selection from user
        try:
            selection = int(input("Make a selection:"))
            
            if selection == 1:
                """check in child"""
                child_name = SetupSunday.menu_options(list(children.keys()),"Enter the child # to check in: ")
                
                if child_name in checked_in_kids:
                    print("This child is already checked in.")
                else:
                    SetupSunday.child_check_in(children[child_name])
                    checked_in_kids.append(child_name)
                print()
            
            elif selection == 2:

                """check out child"""
                if len(checked_in_kids) == 0:
                    print("There are currently no checked in children.")
                    
                else:
                    child_name = SetupSunday.menu_options(checked_in_kids,
                                              "Select # of child to check out: ")
                    SetupSunday.child_check_out(children[child_name])
                    checked_in_kids.remove(child_name)
                print()

            elif selection == 3:
                """setup new child from input"""
                Child.new_from_input(children)
                print()
                
            elif selection == 4:
                """remove child"""
                child_name = SetupSunday.menu_options(list(children.keys()),
                                          "Select # of child to remove: ")
                Child.remove_from_dict(children,child_name)
                if child_name in checked_in_kids:
                    checked_in_kids.remove(child_name)
                print()
                
            elif selection == 5:
                """page guardian"""
                if len(checked_in_kids) == 0:
                    print("There are currently no checked in children.")
                else:
                    child_name = SetupSunday.menu_options(checked_in_kids,
                                          "Select # of child to contact guardian: ")
                    SetupSunday.page_guardian(children[child_name])
                print()

            elif selection == 6:
                """update guardian info"""
                child_name = SetupSunday.menu_options(list(children.keys()),
                                          "Select # of child to update info for: ")
                new_guardian = Validation.validate_alpha(
                               "Enter new guardian name: ")
                new_SMS = Validation.validate_phone(
                               "Enter new SMS phone: ")
                children[child_name].set_guardian_first_name(new_guardian)
                children[child_name].set_SMS_contact(new_SMS)
                print(children[child_name])
                print()
           
            elif selection == 7:
                """check out all kids, quits menu"""
                while len(checked_in_kids) != 0:
                    i = 0
                    children[checked_in_kids[i]].set_is_checked_in(False)
                    checked_in_kids.pop(i)
                    i+= 1
            else:
                raise ValueError
        
        except ValueError:
            print("You made an invalid selection. Try again.")
    
if __name__ == "__main__":
    sample_setup() # run first time only to load sample data
    present_menu()
    

    
    