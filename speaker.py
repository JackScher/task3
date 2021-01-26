import sys

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
            sys.exit()
        else:
            print('Wrong choice.')
            return self.execute()

    def add_new_person(self):               # add_new_person - is right ?
        person_data = self.service.execute()
        new_object = Adapter(self.service.roles, person_data).create_object()
        self.is_new_object_data_valid(new_object)
        return self.execute()

    def check_persons_list(self):
        for group in self.service.roles:
            print('Group ' + group + ':')
            for role in self.service.roles[group]:
                print('Role ' + role + ':')
                for obj in self.service.roles[group][role]:
                    print(obj)
        return self.execute()

    def is_new_object_data_valid(self, new_object):
        main_data = new_object.data_arr
        main_data_info = new_object.main_data_info
        additional_data = new_object.additional_data_arr
        additional_data_info = new_object.additional_data_info
        if new_object.is_valid_data_type(main_data, main_data_info) \
                and new_object.data_item_value_is_not_null(main_data)\
                and new_object.is_valid_data_type(additional_data, additional_data_info)\
                and new_object.data_item_value_is_not_null(additional_data):
            CoreSchool(new_object, self.service.roles).execute()
        else:
            print('Wrong input type. Try again!')
            self.add_new_person()
