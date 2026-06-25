import unittest

from homework_12 import multiplication_table
from homework_12 import put_in
from homework_12 import counter
from homework_12 import Student


class HomeTeste(unittest.TestCase):
    def test_multiplication_table(self):
        actual = multiplication_table(5)
        expected = ['5x1=5', '5x2=10', '5x3=15', '5x4=20', '5x5=25']
        self.assertEqual(actual, expected)

    def test_multiplication_table_less(self):
        actual = multiplication_table(-2)
        expected = []
        self.assertEqual(actual, expected)

    def test_multiplication_table_skipped(self):
        actual = multiplication_table(26)
        self.assertEqual(len(actual), 0)

    def test_list_of_string(self):
        lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']
        actual = put_in(lst1)
        self.assertTrue(all(isinstance(item, str) for item in actual))

    def test_even_number_calculator(self):
        list_1 = [4, 7, 2, 9, 8]
        actual = counter(list_1)
        expected = 14
        self.assertEqual(actual, expected)

    def test_number_calculator(self):
        list_1 = [1, 7, 5, 9, 13]
        actual = counter(list_1)
        self.assertEqual(actual, 0)

    def test_student_creation(self):
        student = Student("Andrii", "Dobranskyi", 30, 95)

        self.assertEqual(student.name, "Andrii")
        self.assertEqual(student.surname, "Dobranskyi")
        self.assertEqual(student.age, 30)

    def test_score_update_int(self):
        student = Student("Andrii", "Dobranskyi", 30, 95)

        student.score_update(100)

        self.assertEqual(student._Student__grade, 100)

    def test_score_update_float(self):
        student = Student("Andrii", "Dobranskyi", 30, 95)

        student.score_update(99.5)

        self.assertEqual(student._Student__grade, 99.5)

    def test_score_update_invalid_value(self):
        student = Student("Andrii", "Dobranskyi", 30, 95)

        with self.assertRaises(ValueError):
            student.score_update("excellent")

if __name__ == '__main__':
    unittest.main()