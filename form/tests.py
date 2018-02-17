from django.test import SimpleTestCase
from .models import Numbers

class NumbersSendTest(SimpleTestCase):
    def test(self):
        a = ['3,4,8,10,57,1,3', '5,6,2,4,29,24,3,4', '1,2,3,4,5,6']
        self.assertEqual(Numbers.numbers_sort(a[0]), '1,3,3,4,8,10,57')
        self.assertEqual(Numbers.numbers_sort(a[1]), '2,3,4,4,5,6,24,29')
        self.assertEqual(Numbers.numbers_sort(a[2]), '1,2,3,4,5,6')
# Create your tests here.
