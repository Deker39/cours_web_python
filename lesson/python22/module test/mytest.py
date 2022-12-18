import unittest
from main_test import FirstSimpleClass,SecondSimpleClass
# from main_test import SimpleCalc,


# class SimpleCalcTestCase(unittest.TestCase):
#     def setUp(self) -> None:
#         self.cals = SimpleCalc()
#
#     def tearDown(self) -> None:
#         print('End test...')
#
#     def test_addition_two_integer(self):
#         result = self.cals.sum(5, 6)
#         self.assertEqual(11, result)
#
#     def test_addition_two_string(self):
#         result = self.cals.sum(3,'asd')
#         self.assertEqual('err2or', result)
#
#     def test_addition_two_bool(self):
#         result = self.cals.sum(-5, -1)
#         self.assertEqual(-6,result)
#         self.assertNotEqual(6, result)

class TestCaseFirstSimpleClass(unittest.TestCase):
    def setUp(self) -> None:
        self.fsc = FirstSimpleClass({1, 2, 3, 4, 5})

    def tearDown(self) -> None:
        print(f'Test completed perfectly...')

    # TODO def sum_set
    def test_sum_set_res_int(self):
        result = self.fsc.sum_set()
        self.assertEqual(15, result)

    def test_sum_set_res_not_str(self):
        result = self.fsc.sum_set()
        self.assertNotEqual('15', result)

    def test_sum_set_res_not_none(self):
        result = self.fsc.sum_set()
        self.assertIsNotNone(result)

    def test_sum_set_res_type(self):
        result = self.fsc.sum_set()
        self.assertIsInstance(result,int)

    # TODO def avg_set
    def test_avg_set_res_int(self):
        result = self.fsc.avg_set()
        self.assertEqual(3, result)

    def test_avg_set_res_not_str(self):
        result = self.fsc.avg_set()
        self.assertNotEqual('3', result)

    def test_avg_set_res_not_none(self):
        result = self.fsc.avg_set()
        self.assertIsNotNone(result)

    def test_avg_set_res_type(self):
        result = self.fsc.avg_set()
        self.assertIsInstance(result,float)

    # TODO def max_set
    def test_max_set_res_int(self):
        result = self.fsc.max_set()
        self.assertEqual(5, result)

    def test_max_set_res_not_str(self):
        result = self.fsc.max_set()
        self.assertNotEqual('3', result)

    def test_max_set_res_not_none(self):
        result = self.fsc.max_set()
        self.assertIsNotNone(result)

    def test_max_set_res_type(self):
        result = self.fsc.max_set()
        self.assertIsInstance(result, int)

    # TODO def min_set
    def test_min_set_res_int(self):
        result = self.fsc.min_set()
        self.assertEqual(1, result)

    def test_min_set_res_not_str(self):
        result = self.fsc.min_set()
        self.assertNotEqual('3', result)

    def test_min_set_res_not_none(self):
        result = self.fsc.min_set()
        self.assertIsNotNone(result)

    def test_min_set_res_type(self):
        result = self.fsc.min_set()
        self.assertIsInstance(result, int)


class TestCaseSecondSimpleClass(unittest.TestCase):

    def setUp(self) -> None:
        self.ssc = SecondSimpleClass(10)

    def tearDown(self) -> None:
        print(f'Test completed perfectly...')

    # TODO def get value
    def test_get_value_int(self):
        self.ssc.value = 10
        result = self.ssc.value
        self.assertEqual(10,result)

    # def test_get_value_str(self):
    #     self.ssc.value = '10'
    #     result = self.ssc.value
    #     self.assertRaises(BaseException('error'),result)



    # TODO def convert_value_to_octal_system
    def test_convert_value_to_octal_system_res_int(self):
        result = self.ssc.convert_value_to_octal_system()
        self.assertEqual(oct(0o12), result)

    def test_convert_value_to_octal_system_res_not_none(self):
        result = self.ssc.convert_value_to_octal_system()
        self.assertIsNotNone(result)

    def test_convert_value_to_octal_system_res_type(self):
        result = self.ssc.convert_value_to_octal_system()
        self.assertIsInstance(result, int)


    # TODO def convert_value_to_hexadecimal_system
    def test_convert_value_to_hexadecimal_system_res_int(self):
        result = self.ssc.convert_value_to_hexadecimal_system()
        self.assertEqual(hex(0xa), result)


    # TODO def convert_value_to_binary_system
    def test_convert_value_to_binary_system_res_int(self):
        result = self.ssc.convert_value_to_binary_system()
        self.assertEqual(bin(0b1010), result)




