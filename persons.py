# class BasePerson:
#     def __init__(self, first_name, last_name, age, role):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age
#         self.role = role
#
#         self.data_arr = [self.first_name, self.last_name, self.age, self.role]
#         self.data_info = {
#             self.first_name: str,
#             self.last_name: str,
#             self.age: int,
#             self.role: str
#         }
#
#     def is_valid_data_type(self):
#         for item in self.data_arr:
#             if self.data_info[item] != type(item):
#                 return False
#         return True
#
#     def data_item_value_is_not_null(self):
#         for item in self.data_arr:
#             if item == '' or item is None:
#                 return False
#         return True
#
#
# class Person(BasePerson):
#     def __init__(self, *args):
#         super().__init__(*args)
#         self._data_arr = []
#         self._data_info = {}
#
#     def is_valid_data_type(self):
#         if super().is_valid_data_type():
#             for item in self._data_arr:
#                 if self._data_info[item] != type(item):
#                     return False
#             return True
#         else:
#             return False
#
#     def data_item_value_is_not_null(self):
#         if super().data_item_value_is_not_null():
#             for item in self._data_arr:
#                 if item == '' or item is None:
#                     return False
#             return True
#         else:
#             return False
#
#     def __str__(self):
#         return '{} {}'.format(self.first_name, self.last_name)
#
#
# class Teacher(Person):
#     def __init__(self, first_name, last_name, age, role, amount, currency, experience_month):
#         super().__init__(first_name, last_name, age, role)
#         self.amount = amount
#         self.currency = currency
#         self.experience_month = experience_month
#
#         self._data_arr = [self.amount, self.currency, self.experience_month]
#         self._data_info = {
#             self.amount: int,
#             self.currency: int,
#             self.experience_month: int,
#         }
#
#
# class Student(Person):
#     def __init__(self, first_name, last_name, age, role, average_mark):
#         super().__init__(first_name, last_name, age, role)
#         self.average_mark = average_mark
#
#         self._data_arr = [self.average_mark]
#         self._data_info = {
#             self.average_mark: int
#         }


class BasePerson:
    def __init__(self, first_name, last_name, age, role):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.role = role
        self.data_arr = [self.first_name, self.last_name, self.age, self.role]

        self.data_info = {
            self.first_name: str,
            self.last_name: str,
            self.age: int,
            self.role: str
        }

        self.additional_data_arr = []
        self.additional_data_info = {}

    def is_valid_data_type(self):
        for item in self.data_arr:
            if self.data_info[item] != type(item):
                return False
        return True

    def data_item_value_is_not_null(self):
        for item in self.data_arr:
            if item == '' or item is None:
                return False
        return True

    def check_additional_data_is_valid(self):
        for item in self.additional_data_info:
            if self.additional_data_info[item] != type(item):
                return False
        return True

    def check_additional_data_is_not_null(self):
        for item in self.additional_data_arr:
            if item == '' or item is None:
                return False
        return True

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)


class Teacher(BasePerson):
    def __init__(self, first_name, last_name, age, role, amount, currency, experience_month):
        super().__init__(first_name, last_name, age, role)
        self.amount = amount
        self.currency = currency
        self.experience_month = experience_month

        self.additional_data_arr = [self.amount, self.currency, self.experience_month]
        self.additional_data_info = {
            self.amount: int,
            self.currency: int,
            self.experience_month: int,
        }


class Student(BasePerson):
    def __init__(self, first_name, last_name, age, role, average_mark):
        super().__init__(first_name, last_name, age, role)

        self.average_mark = average_mark
        self.additional_data_arr = [self.average_mark]
        self.additional_data_info = {
            self.average_mark: int
        }
