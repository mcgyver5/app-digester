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

    def open_war(self,filename):
        print("open war")
        #the job of this function is to return a valid war filehandle or cause an error:
        # has to end with .war and have a valid manifest
        try:
            warfile = open(filename)
            head,tail = os.path.split(warfile.name)
            if not tail.endswith(".war"):
                raise ValueError("needs a war file!")
            return warfile
        except IOError:
            print("file not found")
        except ValueError:
            print("value error")

    def list_files(self,filename):
        zf = zipfile.ZipFile(filename,'r')
        entrylist = zf.infolist()
        for entry in entrylist:
            fn = entry.filename
            head, tail = os.path.split(fn)
            if tail.endswith(".xhtml"):
                print(fn)

    def create_file(self, filename):
        warfile = self.open_war(filename)
        head,tail = os.path.split(warfile.name)
        textfilename = tail.replace(".","_")
        return textfilename+".txt"
