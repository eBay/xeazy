
# *********************************************************
# Copyright 2018 eBay Inc.
# Developer : Karunamoorthy,Elango
# Architect : Gopalakrishnan Karunakaran,Jegan
#
# Use of this source code is governed by an MIT-style
# license that can be found in the LICENSE file or at
# https://opensource.org/licenses/MIT.
# *********************************************************

class htmlParser:

    def readTextFile(self, fileName):
        d = {};
        i = 1
        with open(fileName, 'r') as file:
            for line in file:
                if ('Test Suite' in line) or ('Test Case' in line) or ('t = ' in line) or ('fatal error' in line):
                    print(line)
                    d[i] = line
                    i += 1
        return d

    def feedIntoHtmlTemplate(selfself, d):
        f = open('report2.html','w')
        message = '<html><body><table>'
        color = '#ccddee'
        for key, value in d.iteritems():
            if (key % 2 == 0):
                color = '#ffffff'
            else:
                color = '#ccddee'
            message += '<tr bgcolor="' + color + '"><td>' + value + '</td></tr>'
        message += '<table><body><html>'
        f.write(message)
        f.close()

    def __init__(self, value):
        self.value = value