import unittest
from src.trial_function import say_hi


class TestSayHi(unittest.TestCase):
    def test_instances_valid(self):
        self.assertEqual(say_hi('Name'), f'Well, hi, Name! Nice to meet you!')

    def test_instances_wrong(self):
        wrong_instances = [1, ['Name', 'Surname'], ('Dasha', 'Nastya'), {'Name': 'Surname'}]
        for i in wrong_instances:
            self.assertEqual(say_hi(i), 'Uh-oh! I can only use strings.')

    def test_names_valid(self):
        right = ["Nastya", " Dasha", "Anne-Marie", "Na'vi", "Na’vi", "Louis VI Le Gros", "\nLouis de Batz-Castelmore d'Artagnan "]
        for i in right:
            self.assertEqual(say_hi(i), f'Well, hi, {i.strip()}! Nice to meet you!')

    def test_names_wrong(self):
        wrong = ["I'm Nastya!", "Na`vi", "trial123", "Louis the 6th", "Cool_username"]
        for i in wrong:
            self.assertEqual(say_hi(i), "Sorry, seems like I can't understand you :(")


if __name__ == '__main__':
    unittest.main()
