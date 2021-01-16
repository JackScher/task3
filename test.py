import unittest

from core import CoreSchool
from logic import Logic
from service import Speaker
from utils import roles, main_fields, person_additional_data_fields


class TestCoreSchool(unittest.TestCase):
    def test_create_arr(self):
        correct_person = {'first_name': 'jack', 'last_name': 'scher', 'age': '22', 'role': 'student',
                          'person_additional_data': {'average_mark': '5'}}
        school13 = CoreSchool(roles, correct_person)
        expected_data = ['student', {'first_name': 'jack', 'last_name': 'scher', 'age': '22', 'role': 'student',
                                     'person_additional_data': {'average_mark': '5'}}, 'students']
        self.assertEqual(expected_data, school13.create_arr())


class TestLogic(unittest.TestCase):
    def test_create_right_dictionary(self):
        new_person = { 'first_name': 'jack', 'last_name': 'scher', 'age': '22', 'role': 'student', 'average_mark': '5'}
        logic = Logic(person_additional_data_fields, new_person)
        expected_data = {'first_name': 'jack', 'last_name': 'scher', 'age': '22', 'role': 'student',
                         'person_additional_data': {'average_mark': '5'}}
        self.assertEqual(expected_data, logic.create_right_dictionary())

    def test_get_person_additional_data(self):
        new_person = {'first_name': 'jack', 'last_name': 'scher', 'age': '22', 'role': 'student', 'average_mark': '5'}
        logic = Logic(person_additional_data_fields, new_person)
        expected_data = {'average_mark': '5'}
        self.assertEqual(expected_data, logic.get_person_additional_data())


class TestSpeaker(unittest.TestCase):
    def test_add_person(self):
        sp = Speaker(roles, main_fields, person_additional_data_fields)
        expected_data = {'first_name': 'jack', 'last_name': 'scher', 'age': '22', 'role': 'student',
                         'average_mark': '5'}
        self.assertEqual(expected_data, sp.add_person())

    def test_input_personal_additional_data(self):
        sp = Speaker(roles, main_fields, person_additional_data_fields)
        expected_data = {'amount': '1', 'currency': '1', 'experience_month': '1'}
        self.assertEqual(expected_data, sp.input_personal_additional_data('teacher'))

    def test_input_personal_additional_data_2(self):
        sp = Speaker(roles, main_fields, person_additional_data_fields)
        expected_data = {'average_mark': '1'}
        self.assertEqual(expected_data, sp.input_personal_additional_data('student'))

    def test_create_personal_additional_data(self):
        sp = Speaker(roles, main_fields, person_additional_data_fields)
        expected_data = {'amount': '1', 'currency': '1', 'experience_month': '1'}
        self.assertEqual(expected_data, sp.input_personal_additional_data('teacher'))

    def test_create_personal_additional_data_2(self):
        sp = Speaker(roles, main_fields, person_additional_data_fields)
        expected_data = {'average_mark': '1'}
        self.assertEqual(expected_data, sp.input_personal_additional_data('student'))


if __name__ == '__main__':
    unittest.main()