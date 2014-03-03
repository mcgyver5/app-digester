__author__ = 'mcguit1'
import unittest
import os
from first_digester import Wardigester

class TestDigesterFunctions(unittest.TestCase):
    def setUp(self):
        self.wardigester = Wardigester()

    def test_open_war(self):
<<<<<<< HEAD
        self.assertEqual('dne',self.wardigester.try_war('C:\Users\mcguit1\stupid.war'))
        self.assertEqual('hci.war', self.wardigester.try_war('C:\Users\mcguit1\Desktop\HCI\hci.war'))
        self.assertEqual('mrc-web.war', self.wardigester.try_war('C:\Users\mcguit1\Documents\MRC\mrc-web.war'))
=======
        warfile = self.wardigester.open_war("C:\\Users\\mcguit1\\JUNESAGE\\sagedemo.war")
        head,tail = os.path.split(warfile.name)
        self.assertEquals('sagedemo.war',tail)
        self.assertRaises(IOError,self.wardigester.open_war("C:\\Users\\mcguit1\\JUNESAGE\\bummer.war"))
        self.assertRaises(ValueError,self.wardigester.open_war("C:\Users\mcguit1\JUNESAGE\build.xml"))

    def test_new_file(self):
        self.assertEquals('sagedemo_war.txt',self.wardigester.create_file("C:\\Users\\mcguit1\\JUNESAGE\\sagedemo.war"))
>>>>>>> 4688982553061176d7643654f78b175d62db706b
