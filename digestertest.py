__author__ = 'mcguit1'
import unittest
from first_digester import Wardigester

class TestDigesterFunctions(unittest.TestCase):
    def setUp(self):
        self.wardigester = Wardigester()

    def test_open_war(self):
        self.assertEqual('dne',self.wardigester.try_war('C:\Users\mcguit1\stupid.war'))
        self.assertEqual('hci.war', self.wardigester.try_war('C:\Users\mcguit1\Desktop\HCI\hci.war'))
        self.assertEqual('mrc-web.war', self.wardigester.try_war('C:\Users\mcguit1\Documents\MRC\mrc-web.war'))
