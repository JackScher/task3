from abc import ABC, abstractmethod
from persons import Student


# class SchoolInterface(ABC):
#     @abstractmethod
#     def add_person(self, arr):
#         """add new person to school"""
#         pass
#
#
# class CoreSchool(SchoolInterface):
#     def __init__(self, role, info=None):
#         self.info = info
#         self.role = role
#
#     def add_person(self, arr):
#         group = arr[2]
#         person = arr[1]
#         key = arr[0]
#         self.role[group][key].append(person)
#         print('Person ' + arr[1].first_name + ' ' + arr[1].last_name + ' has been added to ' + arr[2] + '-group with key ' + arr[0])
#
#     def execute(self):
#         arr = self.create_arr()
#         if arr:
#             self.add_person(arr)
#         else:
#             print("wrong role")
#
#     def create_arr(self):
#         arr = None
#         if self.info.role in self.role['teachers'].keys():
#             status = 'teachers'
#             arr = [self.info.role, self.info, status]
#         elif self.info.role in self.role['students'].keys():
#             status = 'students'
#             arr = [self.info.role, self.info, status]
#         return arr


########################################################################################################################


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


########################################################################################################################
# roles = {
#     'teachers': {
#                 'director': [],
#                 'main teacher': [],
#                 'teacher': []
#             },
#     'students': {
#                 'main student': [],
#                 'student': []
#     }
# }
#
# st = Student('jack', 'scher', 23, 'student', 5)
# new = CoreSchool(st, roles)
# # object_i = new.create_object()
# # new.add_person(object_i)
# new.execute()
