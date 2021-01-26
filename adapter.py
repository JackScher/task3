from persons import Teacher, Student


class Adapter:
    def __init__(self, roles, kwargs):
        self.roles = roles
        self.person_data_dict = kwargs

    def create_object(self):
        if self.person_data_dict['role'] in self.roles['students']:
            student = Student(self.person_data_dict)
            return student
        elif self.person_data_dict['role'] in self.roles['teachers']:
            teacher = Teacher(self.person_data_dict)
            return teacher
