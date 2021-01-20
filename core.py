from abc import ABC, abstractmethod


class SchoolInterface(ABC):
    @abstractmethod
    def add_person(self, arr):
        """add new person to school"""
        pass


class CoreSchool(SchoolInterface):
    def __init__(self, role, info=None):
        self.info = info
        self.role = role

    def add_person(self, arr):
        group = arr[2]
        person = arr[1]
        key = arr[0]
        self.role[group][key].append(person)
        print('Person ' + arr[1].first_name + ' ' + arr[1].last_name + ' has been added to ' + arr[2] + '-group with key ' + arr[0])

    def execute(self):
        arr = self.create_arr()
        if arr:
            self.add_person(arr)
        else:
            print("wrong role")

    def create_arr(self):
        arr = None
        if self.info.role in self.role['teachers'].keys():
            status = 'teachers'
            arr = [self.info.role, self.info, status]
        elif self.info.role in self.role['students'].keys():
            status = 'students'
            arr = [self.info.role, self.info, status]
        return arr
