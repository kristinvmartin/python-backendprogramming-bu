Kristin Martin
BU MET CS 521
March 10, 2019
Term Project Submission: README file

*******************
Program Description
*******************

This program is designed to automate the administrative processes involved in Sunday School classes, children's ministry classes,
CCD, or the like. It caters to smaller church communities with fewer than 50 children but could be modified to accommodate larger groups.
The program enables these communities to save time and increase efficiency without the added cost of a more expensive
content management system (also known as Church Management System (CMS) within the industry) that larger churches are more likely
to be able to afford.

For a more robust program option, users can opt to pay for a service like KidCheck (https://www.kidcheck.com) or review other options
at https://www.childrens-ministry-deals.com/blogs/childrens-pastors-only/childrens-ministry-check-in-system.

******************
How to Run Program
******************

The initial program setup is designed to be run before students arrive.  The user should load Child.py,SundaySchoolClass.py, and 
Validation.py before attempting to launch the main progam file, BeginSunday.py.  For the convenience of testing the program and showing its
functionality, classroom categories and age groups are pre-loaded (as they are essentially static once established with few exceptions),
and there are a few sample "children" pre-loaded into the program as well.

Once the modules are loaded, the user can set up the classes for the day by running the BeginSunday.py module.  The user will be prompted
first to enter and verify the teachers assigned to the pre-loaded categories of classes. Once completed, the user will be presented with
a menu for the most common usages of the program.  Children should be added from the menu option using user input to ensure proper validation
Follow the in-line comments, docstrings, and class directories for further insight on 
other potential usages.

****************************
What It Looks Like In Action
****************************

After all files are loaded, the user executes BeginSunday.py and this is displayed:

*************************************************************************
Welcome to church!
Please set up your teacher and classroom assignments before beginning.
Use Teachers.txt to adjust your teachers for the week.          
Do NOT change the categories. Save the file when done.

Type 'go' when ready to load:
*************************************************************************

The user should modify the teachers' names in the included Teachers.txt file and save it.
The user should NOT modify the categories listed unless also modifying the categories
tuple in the sample setup.
Once completed and the user signals the program by typing 'go', a confirmation is printed:

*************************************************************************
Type 'go' when ready to load:go

Great!  Your teacher assignments for today are:

Nursery class on 2019-03-10 is being taught by Tricia
Preschool class on 2019-03-10 is being taught by Stephanie
Grade School class on 2019-03-10 is being taught by Kristin
Teenagers class on 2019-03-10 is being taught by Brooke
*************************************************************************

Then, the user is presented a menu of actions.  Once a selection is made an the action is
completed, the menu is presented again (unless the user chooses the option to quit).

*************************************************************************
Welcome to the main menu! Here's what you can do: 

1: Check a child into class that's already been here
2: Check out a child that is in currently in a class
3: Set up a new child
4: Remove a child from the current directory of students
5: Page a parent/guardian
6: Update parent/guardian information of a previously set up child
7: Close the Sunday School and check out all children.

Make a selection:
*************************************************************************

There are pre-loaded sample "children" to test the program and error handling is in place
if the user passes invalid input.  Go explore and enjoy!



**********************
Other Relevant Details
**********************
Due to the widely varying needs of churches and their available capital, the "Page a Guardian"
functionality currently just returns the SMS contact phone number of the assigned guardian and
displays identifying information.  This is so churches can decide to either simply have the teacher
text or call the parent, relay the information to a media worker (who can impose the message onto
a screen in the church sanctuary/meeting room), or, if there are available funds, use a third-party
module and API like Twilio to send SMS messages directly from this program.

Further plans for implementation include: logging check-in and check-out in a file to enable
historical data tracking, reading child data from an outside file to create new children,
more robust txt file reading for teacher assignments including dynamic categories and age-group setups.

