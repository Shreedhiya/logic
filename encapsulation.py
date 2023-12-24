class employee:
    def __init__(self,name,id,salary):
        self.name=name
        self.id=id
        self.salary=salary

    def getempsalary(self):
        print("\n Employee name:",self.name)
        print("Employee id:",self.id)
        print("Employee salary:",self.salary)

emp1=employee("liya",123,20000)
emp2=employee("sandy",234,20000)

emp1.getempsalary()
emp2.getempsalary()

