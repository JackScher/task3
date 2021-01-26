class BasePerson:
    def __init__(self, person_data_dict):
        for name, value in person_data_dict.items():
            try:
                setattr(self, name, int(value))
            except:
                setattr(self, name, value)

        self.data_arr = [self.first_name, self.last_name, self.age, self.role]
        self.main_data_info = {
            self.first_name: str,
            self.last_name: str,
            self.age: int,
            self.role: str
        }

        self.additional_data_arr = []
        self.additional_data_info = {}

    def is_valid_data_type(self, input_fields_arr, right_fields_info):
        for item in input_fields_arr:
            if right_fields_info[item] != type(item):
                return False
        return True

    def data_item_value_is_not_null(self, input_fields_arr):
        for item in input_fields_arr:
            if item == '' or item is None:
                return False
        return True

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)


class Teacher(BasePerson):
    def __init__(self, person_data_dict):
        super().__init__(person_data_dict)

        self.additional_data_arr = [self.amount, self.currency, self.experience_month]
        self.additional_data_info = {
            self.amount: int,
            self.currency: int,
            self.experience_month: int,
        }


class Student(BasePerson):
    def __init__(self, person_data_dict):
        super().__init__(person_data_dict)

        self.additional_data_arr = [self.average_mark]
        self.additional_data_info = {
            self.average_mark: int
        }
