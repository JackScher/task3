class Logic:
    def __init__(self, person_additional_data, dictionary):
        self.data = dictionary
        self.person_additional_data_fields = person_additional_data

    def create_right_dictionary(self):
        person_additional_data = self.get_person_additional_data()
        for key in person_additional_data.keys():
            del self.data[key]
        return self.data

    def get_person_additional_data(self):
        person_additional_data = {}
        for arr_key in self.person_additional_data_fields:
            for field in self.person_additional_data_fields[arr_key]:
                for key in self.data:
                    if field == key:
                        person_additional_data[field] = self.data[key]
        self.create_person_additional_data(person_additional_data)
        return person_additional_data

    def create_person_additional_data(self, data):
        keys = []
        for data_key in data.keys():
            if data_key in self.person_additional_data_fields['students']:
                self.data['person_additional_data'] = data
            else:
                for key in data:
                    if key == 'amount' or key == 'currency':
                        self.data['person_additional_data'] = {'salary': {}}
                        keys.append(key)
                    else:
                        self.data['person_additional_data'][key] = data[key]
                self.create_salary_field(keys, data)

    def create_salary_field(self, keys, data):
        for key in keys:
            self.data['person_additional_data']['salary'][key] = data[key]
