__author__ = 'mcguit1'
import os
import zipfile
import Tkinter, tkFileDialog

#start with war file

#use py zip libraries to loop through and find all web files (jsp, xhtml, html, etc)

# make a list of paths in a text file

def skip():
    pass


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
            textfilename = self.create_file(warfile.name)
            textfilename = "tfiles/" + textfilename
            head,tail = os.path.split(warfile.name)
            if not tail.endswith(".war"):
                raise ValueError("needs a war file!")

            zf = zipfile.ZipFile(filename, 'r')
            file_list = zf.infolist()
            print("can it open:")
            textFile = open(textfilename,'w')
            for entry in file_list:
                fileNa = entry.filename
                #exclude images, stylesheets:

                extensions = ('.js','.class','.png', '.jpg','.gif','.css')

                head,tail = os.path.split(fileNa)
                if any (tail.endswith(ext) for ext in extensions):
                    skip()
                else:
                    print(entry.filename)
                    textFile.write(entry.filename + "\n")
            textFile.close()
            head,tail = os.path.split(filename)
            return tail

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
        head,tail = os.path.split(filename)
        textfilename = tail.replace(".","_")
        return textfilename+".txt"

w = Wardigester()

root = Tkinter.Tk()
root.withdraw()

file_path = tkFileDialog.askopenfilename()
w.open_war(file_path)
