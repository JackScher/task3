from abc import ABC, abstractmethod


class CreateObjectForSave:
    def __init__(self, status, person_information, role):
        self.status = status
        self.person_information = person_information
        self.role = role


class AbstractSchool(ABC):
    def create_object(self):
        if self.person_info.role in self.role_dictionary['teachers'].keys():
            status = 'teachers'
        elif self.person_info.role in self.role_dictionary['students'].keys():
            status = 'students'
        person_info_object = CreateObjectForSave(status, self.person_info, self.person_info.role)
        return person_info_object

    def add_person(self, person_info_object):
        group = person_info_object.status
        person = person_info_object.person_information
        role = person_info_object.role
        self.role_dictionary[group][role].append(person)
        print('Person ' + person.first_name + ' ' + person.last_name + ' has been added to ' + group + '-group with key ' + role)

    def execute(self):
        person_info_object = self.create_object()
        if person_info_object:
            self.add_person(person_info_object)
        else:
            print("wrong role")


class CoreSchool(AbstractSchool):
    def __init__(self, person_object, role_dictionary):
        self.person_info = person_object
        self.role_dictionary = role_dictionary
