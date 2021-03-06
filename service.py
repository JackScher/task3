class Service:
    def __init__(self):
        self.roles = {
            'teachers': {
                    'director': [],
                    'main teacher': [],
                    'teacher': []
            },
            'students': {
                    'main student': [],
                    'student': []
            }
        }
        self.main_fields = ['first_name', 'last_name', 'age', 'role']
        self.person_additional_data_fields = {
                'teachers': ['amount', 'currency', 'experience_month'],
                'students': ['average_mark']
        }

    def execute(self):
        input_data = {key: input('Input ' + key + ':') for key in self.main_fields}
        if input_data['role'] in self.roles['teachers'] or input_data['role'] in self.roles['students']:
            additional_data = self.input_personal_additional_data(input_data['role'])
            input_data.update(additional_data)
            return input_data
        else:
            print('Wrong role. Try again!')
            return self.execute()

    def input_personal_additional_data(self, role):
        additional_data_dict = {}
        if role in self.roles['teachers']:
            additional_data_dict = self.create_personal_additional_data_dict('teachers')
        elif role in self.roles['students']:
            additional_data_dict = self.create_personal_additional_data_dict('students')
        return additional_data_dict

    def create_personal_additional_data_dict(self, mode):
        fields = [field for field in self.person_additional_data_fields[mode]]
        additional_data_arr = {key: input('Input ' + key + ':') for key in fields}
        return additional_data_arr
