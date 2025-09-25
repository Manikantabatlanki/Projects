from abc import ABC, abstractmethod

# Abstract Base Class
class Employee(ABC):
    def _init_(self, name, base_salary):
        self.name = name
        self._base_salary = base_salary  # Protected attribute
        self.__bonus = 0  # Private attribute

    @abstractmethod
    def calculate_salary(self):
        pass  # Must be implemented by subclasses

    def set_bonus(self, amount):
        self.__bonus = amount

    def get_bonus(self):
        return self.__bonus

# Subclass 1
class Developer(Employee):
    def _init_(self, name, base_salary, programming_language):
        super()._init_(name, base_salary)
        self.programming_language = programming_language

    def calculate_salary(self):
        return self._base_salary + self.get_bonus()

# Subclass 2
class Manager(Employee):
    def _init_(self, name, base_salary, team_size):
        super()._init_(name, base_salary)
        self.team_size = team_size

    def calculate_salary(self):
        # Managers get extra pay for team size
        return self._base_salary + (self.team_size * 1000) + self.get_bonus()

# Using Polymorphism
employees =[Developer("Alice", 50000, "Python"),Manager("Bob", 60000, 5)]

# Setting bonuses
employees[0].set_bonus(5000)  # Developer bonus
employees[1].set_bonus(8000)  # Manager bonus

# Display results
for emp in employees:
    print(f"{emp.name}'s Salary: {emp.calculate_salary()}")
    print(f"Bonus: {emp.get_bonus()}")
    print("Type:", emp._class.name_)
    print("-" * 30)
