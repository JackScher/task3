from core import CoreSchool
from logic import Logic
from utils import roles, person_additional_data_fields


class Speaker:
    def __init__(self, roles_dictionary, necessary_fields, person_additional_data):
        self.roles = roles_dictionary
        self.main_fields = necessary_fields
        self.person_additional_data_fields = person_additional_data

    def add_person(self):
        data = {key: input('Input ' + key + ':') for key in self.main_fields}
        if data['role'] in self.roles['teachers'] or data['role'] in self.roles['students']:
            additional_data = self.input_personal_additional_data(data['role'])
            data.update(additional_data)
            return data
        else:
            print('Wrong role. Try again!')
            return self.add_person()

    def input_personal_additional_data(self, role):
        arr = []
        if role in self.roles['teachers']:
            arr = self.create_personal_additional_data('teachers')
        elif role in self.roles['students']:
            arr = self.create_personal_additional_data('students')
        return arr

    def create_personal_additional_data(self, mode):
        fields = [field for field in self.person_additional_data_fields[mode]]
        arr = {key: input('Input ' + key + ':') for key in fields}
        return arr

    def execute(self):
        print('Hello. 1-to add new person. 2-to check the list of persons. 3-to end.')
        choice = input()
        self.your_choice(choice)

    def your_choice(self, choice):
        if choice == '1':
            self.choice1()
        elif choice == '2':
            self.choice2()
        elif choice == '3':
            return True
        else:
            print('Wrong choice.')
            return self.execute()

    def choice1(self):
        new_person = self.add_person()
        logic = Logic(person_additional_data_fields, new_person)
        correct_person = logic.create_right_dictionary()
        school13 = CoreSchool(roles, correct_person)
        school13.execute()
        return self.execute()

    def choice2(self):
        for group in roles:
            print('Group ' + group + ':')
            for rank in roles[group]:
                print('Rank ' + rank + ':')
                for person in roles[group][rank]:
                    print(person)
        return self.execute()
