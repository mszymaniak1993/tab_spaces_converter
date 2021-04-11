import unittest
import converter

class TestZadanie(unittest.TestCase):

    def test_conversion_type(self):
        conv_type_1 = "SPAces"
        conv_type_2 = "TABS"

        self.assertEqual(conv_type_1.lower(), 'spaces')
        self.assertEqual(conv_type_2.lower(), 'tabs')

    def test_need_backup(self):
        need_backup_1 = 'y'
        need_backup_2 = 'n'
        need_backup_3 = 'ok'
        need_backup_4 = ':)'
        need_backup_5 = None
        need_backup_6 = ''

        self.assertIsNotNone(need_backup_1, True)
        self.assertIsNotNone(need_backup_2, True)
        self.assertIsNotNone(need_backup_3, True)
        self.assertIsNotNone(need_backup_4, True)
        self.assertIsNone(need_backup_5, True)
        self.assertIsNotNone(need_backup_6, False)

    def test_number_of_spaces(self):
        number_1 = 9
        number_2 = 4
        number_3 = None

        self.assertEqual(number_1, 9)
        self.assertEqual(number_2, 4)
        self.assertIsNone(number_3, 4)

if __name__ =="__main__":
    unittest.main()