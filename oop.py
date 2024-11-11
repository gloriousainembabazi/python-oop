#oop (object oriented programing)
#these are properties
#it is always having properties and attributes
#it is always having classes and objects
#an object is the properties of a class
#class consists of forexample:object,student,name etc


#syntax of oop
#creating classes
#cohort  class
#name start with capital letters and always in singular
class cohort:
  name="Glorious"
description ="cohort class"
Start_date ="20th August 2024"
end_date ="2026"
print(cohort)

#within the cohort class,
#add a constructor for the cohort class.(read about constructors and object/instance)
#add a method to the class that prints the cohort name and the total number of students.
#create a new insance/object of the cohort class.


# adding a constructor
class cohort:
    def __init__(self,name,description,start_date,end_date):
        self.name=name
        self.description=description
        self.start_date=start_date
        self.end_date =end_date
        cohort=cohort('Glorious','cohort class','20th August','2026')
        print(cohort.name)
        print(cohort.description)
        print(cohort.start_date)
        print(cohort.end_date)

 # List of student names
        class Cohort:
        
         def _init_ (self,name,total_student):
          self.name = name
          self.total_student =total_student
           

          def print_cohort_info(self):
        # This method prints the cohort name and total number of students
            print(f"Cohort Name: {self.name}")
        print (f"total number of students:{self.total_student}")





    



