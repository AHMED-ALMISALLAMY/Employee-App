class Employee:
    def __init__(self, name, id, age, departement, is_manager) -> None:
        self.name = name
        self.id = id
        self.age = age
        self.departement = departement
        self.is_manager = is_manager

    def view_details(self):
        print("Employee details profile")
        print("Name is", self.name)
        print("ID:", self.id)
        print("Age:", self.age)
        print("Departement:", self.departement)
        print("Is Manager =>", self.is_manager)