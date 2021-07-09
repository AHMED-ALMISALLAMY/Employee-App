class Employee:
    def __init__(self, name, id, age, departement,salary,experiance, is_manager) -> None:
        self.name = name
        self.id = id
        self.age = age
        self.departement = departement
        self.salary = salary
        self.experiance = experiance
        self.is_manager = is_manager

    def view_details(self):
        print("Employee details profile")
        print("Name is", self.name)
        print("ID:", self.id)
        print("Age:", self.age)
        print("Departement:", self.departement)
        print("Experiance is:", self.experiance)
        print("Your salary:", self.salary)
        print("Is Manager =>", self.is_manager)
        
    def bonus(self):
        if self.experiance > 3:
            self.salary += 20000
            print("Your Salary Increase To " + str(self.salary) + " per year")
        else:
            print("Your salary is " + str(self.salary) + " per year")
        
