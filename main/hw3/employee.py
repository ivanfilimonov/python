class Employee:

    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.salary = self.getValidatedSalary(salary)
        self.full_name = (first_name + ", " + last_name).title()
        self.email = self.getEmail(first_name, last_name)

    def getEmail(self, first_name, last_name):
        return (first_name + "_" + last_name + "@example.com").lower()

    def getValidatedSalary(self, salary):
        if (type(salary) is int):
            return salary
        elif (type(salary) is str and salary.isdigit()):
            return int(salary)
        else:
            raise ValueError("Unexpected value - " + salary)

    @property
    def full_name(self):
        return self._full_name

    @full_name.setter
    def full_name(self, value):
        self._full_name = value.title()
        self.first_name = self._full_name.split(', ')[0]
        self.last_name = self._full_name.split(', ')[1]

    @full_name.deleter
    def full_name(self):
        del self._full_name

    @classmethod
    def from_str(cls, info_str):
        return cls(*info_str.split(","))


class Manager(Employee):
    def __init__(self, *args):
        super().__init__(args[0], args[1], args[2])
        if(args.__len__() > 3): self.subordinates = args[3]
        else: self.subordinates = []

    def add_subordinate(self, new_subordinate):
        if(new_subordinate not in self.subordinates):
            self.subordinates.append(new_subordinate)

    def remove_subordinate(self, subordinate):
        if (subordinate in self.subordinates):
            self.subordinates.remove(subordinate)
        elif (type(subordinate) is str):
            self.subordinates.remove(self.findSubordinateByEmail(subordinate))
        else: print("Subordinate <" + subordinate.full_name +
                    "> does not present in the list of subordinates for manager <" + self.full_name +
                    ">")

    def findSubordinateByEmail(self, email):
        for subordinate in self.subordinates:
            if (subordinate.email == email): return subordinate
        print("Email <" + email +
              "> does not present in the list of subordinates for manager <" + self.full_name +
              ">")


class DevOps(Employee):
    def __init__(self, *args):
        super().__init__(args[0], args[1], args[2])
        if(args.__len__() > 3): self.skills = args[3]
        else: self.skills = []

    def add_skill(self, skill):
        if(skill.title() not in self.skills):
            self.skills.append(skill.title())

    def remove_skill(self, skill):
        if(skill.title() in self.skills):
            self.skills.remove(skill.title())

