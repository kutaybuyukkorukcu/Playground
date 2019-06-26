class Employee():
    def __init__(self, name, salary, department):
        self.name = name
        self.salary = salary
        self.department = department

    def display_results(self):
        print("Displaying the information of the working class")
        print("Name:", self.name, "Salary:", self.salary,
              "Department:", self.department)

    def search_salary(self, raise_amount):
        print("salary is raised")
        self.salary += raise_amount

    def change_department(self, new_department):
        print("Changing department...")
        self.department = new_department

# class Manager(Employee, someKindOfGodOfWar)


class Manager(Employee):
    def __init__(self, name, salary, department, number_of_worker):
        super().__init__(name, salary, department)
        self.number_of_worker = number_of_worker

        def display_results(self):
            print("Displaying the information of manager class")
            print("Name:", self.name, "Salary:", self.salary, "Department:",
            self.department, "Number of Workers", self.number_of_worker)

        def increase_number_of_worker(self, inc):
            print("Increasing number of worker")
            self.number_of_worker += inc

        manager = Manager("Kutay Buyukkorukcu", 0, "Broke Student :)", 20)

    manager.display_results()


manager.increase_number_of_worker(10)
manager.display_results()
