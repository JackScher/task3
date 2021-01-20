from service import Service
from adapter import Adapter
from core import CoreSchool


class Speaker:
    def __init__(self):
        self.service = Service()

    def execute(self):
        print('Hello. 1-to add new person. 2-to check the list of persons. 3-to end.')
        choice = input()
        self.your_choice(choice)

    def your_choice(self, choice):
        if choice == '1':
            self.add_new_person()
        elif choice == '2':
            self.check_persons_list()
        elif choice == '3':
            return True
        else:
            print('Wrong choice.')
            return self.execute()

    def add_new_person(self):
        person_data = self.service.execute()
        adapter = Adapter(self.service.roles, person_data)
        new_object = adapter.create_object()
        if new_object.is_valid_data_type() and new_object.data_item_value_is_not_null():
            CoreSchool(self.service.roles, new_object).execute()
        else:
            print('Wrong input type. Try again!')
            self.add_new_person()
        return self.execute()

    def check_persons_list(self):
        for group in self.service.roles:
            print('Group ' + group + ':')
            for role in self.service.roles[group]:
                print('Role ' + role + ':')
                for obj in self.service.roles[group][role]:
                    print(obj)
        return self.execute()