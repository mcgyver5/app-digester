__author__ = 'mcguit1'
import unittest
from first_digester import Wardigester

class TestDigesterFunctions(unittest.TestCase):
    def setUp(self):
        self.wardigester = Wardigester()

    def test_open_war(self):
        self.assertEquals('sagedemo.war',self.wardigester.open_war("C:\\Users\\mcguit1\\JUNESAGE\\sagedemo.war"))
        self.assertEqual('dne', self.wardigester.open_war("C:\\users\\hci.war"))
        self.assertEqual('dne', self.wardigester.open_war("C:\\users\\mrc-web.war"))
