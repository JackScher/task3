from persons import Teacher, Student


class Adapter:
    def __init__(self, roles, kwargs):
        self.roles = roles
        for name, value in kwargs.items():
            try:
                setattr(self, name, int(value))
            except:
                setattr(self, name, value)

    def create_object(self):
        if self.role in self.roles['students']:
            student = Student(self.first_name, self.last_name, self.age, self.role, self.average_mark)
            return student
        elif self.role in self.roles['teachers']:
            teacher = Teacher(self.first_name, self.last_name, self.age, self.role, self.amount, self.currency, self.experience_month)
            return teacher
