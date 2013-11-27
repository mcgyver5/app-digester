__author__ = 'mcguit1'
import unittest
from first_digester import Wardigester

class TestDigesterFunctions(unittest.TestCase):
    def setUp(self):
        self.wardigester = Wardigester()

    def test_open_war(self):
        self.assertEqual('hci.war', self.wardigester.open_war('C:\Users\mcguit1\Desktop\HCI\hci.war'))
        self.assertEqual('mrc-web.war', self.wardigester.open_war('C:\Users\mcguit1\Documents\MRC\mrc-web.war'))
