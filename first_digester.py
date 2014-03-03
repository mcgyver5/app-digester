__author__ = 'mcguit1'
import os
import zipfile
#start with war file

#use py zip libraries to loop through and find all web files (jsp, xhtml, html, etc)

# make a list of paths in a text file

class Wardigester():
    def about(self):
        return "appdigester version 0.1 alpha"

    def try_war(self,filename):


        if os.path.exists(filename):
            zf = zipfile.ZipFile(filename, 'r')
            file_list = zf.infolist()
            for entry in file_list:
                print(entry.filename)
            warfile = file(filename)
            head,tail = os.path.split(filename)
            return tail
        else:
            return "dne"

