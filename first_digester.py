__author__ = 'mcguit1'
import zipfile
import os

#start with war file

#use py zip libraries to loop through and find all web files (jsp, xhtml, html, etc)

# make a list of paths in a text file

class Wardigester():
    def about(self):
        return "appdigester version 0.1 alpha"

    def open_war(self,filename):
        if os.path.exists(filename):
            zf = zipfile.ZipFile(filename,'r')
            entrylist = zf.infolist()
            for entry in entrylist:

                print(entry.filename)
            warfile = open(filename)
            head,tail = os.path.split(warfile.name)
            return tail
        else:
            return "dne"