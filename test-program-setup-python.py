import sys
print(sys.executable)
print(sys.version)


class Employee:
    """docstring for Employee."""

    def __init__(self, first, last):
        self.first = first
        self.last = last

    def test_method(self):
        pass

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{}.{}'.format(self.first, self.last)


emp_1 = Employee('John', 'Duo')

print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)

for u in range(10):
    print(u)
