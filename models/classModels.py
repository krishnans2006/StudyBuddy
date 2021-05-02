c_daysList = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]

class Class:
    #This is crude, but basically one placeholder for the time a class
    #meets each weekday. A None value indicates that the class does #not meet.
    d_days = ["None"]*7

    def __init__(self, name = None, description = None, days = d_days, teacher = None):
        self.name = name
        self.description = description
        self.days = days
        self.at = self.days
        self.teacher = teacher
        self.subject = self.teacher

class Task:
  def __init__(self, name = None, subject = None, description = None, dueDate = None):
    self.name = name
    self.subject = subject
    self.description = description
    self.dueDate = dueDate
    self.at = self.dueDate.strftime("%m/%d/%y")

class Exam:
  def __init__(self, name = None, subject = None, description = None, datee = None):
    self.name = name
    self.subject = subject
    self.description = description
    self.date = datee
    self.at = self.date.strftime("%m/%d/%y at %I:%M %p")

class User:
  def __init__(self, lastName = None, firstName = None, schoolID = None):
    self.lastName = lastName
    self.firstName  = firstName
    self.schoolID = schoolID
    self.fullName = None