class Employee(object):
   next_employee_number = 0

   def __init__(self, name, hours_worked=0, hourly_rate=9.25):
      self.name = name
      self.id = Employee.next_employee_number
      self.hours_worked = hours_worked
      self.hourly_rate = hourly_rate

      Employee.next_employee_number = Employee.next_employee_number + 1

   def add_hours(self, h):
      self.hours_worked = self.hours_worked + h

   def __str__(self):
      l = []
      l.append("Name: {}".format(self.name))
      l.append("ID: {}".format(str(self.id)))
      l.append("Hours: {:.2f}".format(self.hours_worked))
      l.append("Rate: {:.2f}".format(self.hourly_rate))
      l.append("Wages: {:.2f}".format(self.hourly_rate * self.hours_worked))
      return "\n".join(l)
