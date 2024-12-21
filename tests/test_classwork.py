import unittest
from src.classwork import *


class TestFiplPipl(unittest.TestCase):
    """
    Нам необходимо написать 4 вида тестирования:
    - позитивное
    - негативное
    - граничное
    - тестирование состояния
    """
    def setUp(self):
        self.fipl_pipl = FiplPipl(24)

    def test_postpone_negative(self):
        with self.assertRaises(ValueError):
            self.fipl_pipl.postpone(-1)

    def test_procrastinate_negative(self):
        with self.assertRaises(ValueError):
            self.fipl_pipl.procrastinate(-1)

    def test_procrastinate_overflow(self):
        with self.assertRaises(MissedDeadlineError):
            self.fipl_pipl.procrastinate(25)

    def test_postpone_positive(self):
        self.assertEqual(self.fipl_pipl.postpone(5), 29)

    def test_procrastinate_positive(self):
        self.assertEqual(self.fipl_pipl.procrastinate(5), 19)

    def test_check_deadline_positive(self):
        self.assertEqual(self.fipl_pipl.check_deadline(), 24)


if __name__ == '__main__':
    unittest.main()
