__author__ = 'mcguit1'

#start with war file

#use py zip libraries to loop through and find all web files (jsp, xhtml, html, etc)

# make a list of paths in a text file

class Wardigester():
    def about(self):
        return "appdigester version 0.1 alpha"

    def open_war(self,filename):
        warfile = file(filename)
        return warfile.name