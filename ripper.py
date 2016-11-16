#libraries
import sys
import urllib
from HTMLParser import HTMLParser
from bs4 import BeautifulSoup

#global variables
tags = []

#classes

#color class for printing text in color
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

#functions

#handles the user input
def parseInput ():
    appname = sys.argv[0]
    #checks if the user specified a link
    try:
        sys.argv[1]
    except IndexError:
        print(bcolors.FAIL + "error, no target link specified. add --help for help " + bcolors.ENDC)
        sys.exit()
    else:
        link = str(sys.argv[1])
    #checks if the user specifed an output file
    try:
        sys.argv[2]
    except IndexError:
        print(bcolors.FAIL + "error, no output file specified. add --help for help" + bcolors.ENDC)
        sys.exit()
    else:
        outputFile = open(str(sys.argv[2]),'a+', 1)
    #checks which tags the user is looking for
    taglist = raw_input(bcolors.OKBLUE + "Please specify the tags, divided by a space (leave blank for no filtering): " + bcolors.ENDC)
    tags = taglist.split()
    gethtml(link, outputFile,tags)

#retrieves the html from the given link
def gethtml (link, outputFile, tags):
    page = urllib.urlopen(link)
    pagecontent = page.read()
    print(bcolors.OKGREEN + "succesfully retreived file from internet" + bcolors.ENDC)
    parsefile(pagecontent, outputFile, tags)


#finds the tags from the file and outputs them to the file
def parsefile (document, outputFile, tags):
    print(bcolors.OKGREEN + "starting parsing process..." + bcolors.ENDC)
    if (len(tags) > 0):
        print(bcolors.OKGREEN + "parsing file..." + bcolors.ENDC)
        soup = BeautifulSoup(document, 'html.parser')
        output = soup.findAll(tags)
        soup = BeautifulSoup(str(output), 'html.parser')
        soup = soup.prettify()
        outputFile.write(soup)
        outputFile.close()
        print(bcolors.OKGREEN + "done" + bcolors.ENDC)
    else:
        print (bcolors.WARNING + "no tags given, dumping entire file.." + bcolors.ENDC)
        outputFile.write(str(document))
        outputFile.close()
#code
if ('--help' in sys.argv):
    print(bcolors.OKBLUE + "usage: python " + sys.argv[0] + " targetlink outputfile" + bcolors.ENDC)
else:
    parseInput()
