#! /usr/bin/env python
#

try:
    from IPython import ColorANSI
    from  IPython.genutils import Term
    tc = ColorANSI.TermColors()
except:
    from IPython.utils import coloransi
    tc = coloransi.TermColors()

import sys

"""
 Script to edit text in a large number of files. User is prompted for
the text to be replaced and the text to replace with.  dirList is a
list of all files to search in:

dirtList = "part10/Bulgarelli_O05/Bulgarelli_O05.tex", "part10/Csepany_O09/Csepany_O09.tex", "part10/Currie_P61/Currie_P61.tex", "part10/Diaz_P54/Diaz_P54.tex", "part10/Dowell_P42/Dowell_P42.tex", "part10/Kuemmel_P049/Kuemmel_P049.tex"]

The script will prompt the user whether or not to replace each occurance 0=y 1=n (default is no)

Original Author: D. N. Friedel
"""

dirList = sys.argv[1:]

toIndex = raw_input("Text to edit: ")

# uncomment the line below if you want to do a case insensitive match
#toIndex = toIndex.upper()

# this is case sensitive
indxWith = raw_input("Edit to: ")

replaceTxt = indxWith

for fl in dirList :
    handle = open(fl,'r')
    lines = handle.readlines()
    handle.close()
    outLines = []
    found = False
    print fl
    for line in lines :
        tline = line   #.upper()    #may want to uncomment the upper if you want case insensitive searches
        s = tline.find(toIndex)
        while(s >= 0) :
            skip = False
            last = tline.rfind(".",0,s)
            last = max(0,last)
            next = tline.find(".",s)
            lnext = tline.find("\n",s)
            if(next < 0) :
                next = 1000000
            if(lnext < 0) :
                lnext = 10000000
            end  = min(next,lnext)
            if(not skip) :
                sentence = line[last:s] + tc.Yellow + line[s:s+len(toIndex)] + tc.Normal + line[s+len(toIndex):end]
                print sentence
                ans1 = raw_input("Edit? (0=y,[1]=n): ")
                if(len(ans1) == 0) :
                    ans1 = "2"
                ans = int(ans1)
                if(ans == 0) :
                    found = True
                    line = line[:s] + replaceTxt + line[s + len(toIndex):]
                    tline = line.upper()
                    s = tline.find(toIndex,s+len(toIndex))
                else :
                    s = tline.find(toIndex,s+ len(toIndex))
            else :
                s = tline.find(toIndex,s+ len(toIndex))
        outLines.append(line)
    if(found) :
        handle = open(fl,'w')
        for line in outLines :
            handle.write(line)
        handle.close()
