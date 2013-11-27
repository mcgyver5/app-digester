app-digester
============

searches web application source code for URLs to pass to a scanner

Unlinked web pages in a web applicaton might get missed by a scanner or "black box" assessment.  If the security tester has access to source code or compiled war file, might as well cheat and grab undocumented or hidden directories and files and pass them to scanner of your choice. 

Features:
look through war file or zip of PHP source code and returns a list of paths to web files

Future:  parse web.xml or struts.xml to find URLs that are methods instead of actual web files. 
