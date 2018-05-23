#!/usr/bin/env python
__author__ = 'ekarunamoort'

# *********************************************************
# Copyright 2018 eBay Inc.
# Developer : Karunamoorthy,Elango
# Architect : Gopalakrishnan Karunakaran,Jegan
#
# Use of this source code is governed by an MIT-style
# license that can be found in the LICENSE file or at
# https://opensource.org/licenses/MIT.
# *********************************************************

import argparse
from src import Xcprocessor as xc
from jinja2 import Environment, FileSystemLoader
import os
import shutil
import errno

def main(args):
    print(args.report)
    data = []
    with open('multiple_suite.txt', 'r') as f:
        pipeData = f.readlines()

    x = xc.Xcprocessor()
    responseObj = x.processXC(pipeData)
    template_dir = '../templates'
    env = Environment(
        loader=FileSystemLoader(template_dir)
    )
    template = env.get_template('template.html')
    output_from_parsed_template = template.render(suites=responseObj.suites,response=responseObj)
    with open("../templates/dashboard.html", "wb") as fh:
        fh.write(output_from_parsed_template)

    outputDirectory = args.output
    outputDirectoryPath = outputDirectory+"/xeazy-output/"
    print(outputDirectoryPath)
    try:
        os.makedirs(os.path.dirname(outputDirectoryPath))
    except OSError as exc: # Guard against race condition
        if exc.errno != errno.EEXIST:
            raise
    shutil.rmtree( outputDirectoryPath)
    shutil.copytree("../templates/assets", outputDirectoryPath+"/assets")
    shutil.move("../templates/dashboard.html", outputDirectoryPath+"/dashboard.html")
    writeToFile(pipeData,outputDirectoryPath)

def writeToFile(pipeData,outputDir):
    print "Opening the debug file..."
    target = open(outputDir+'/rawOutput.txt', 'w')
    target.truncate()
    for line in pipeData:
        target.write(line)
    target.close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-r','--report',required=True,choices=['html'], help='report html')
    parser.add_argument('-o','--output',required=True, help='output files to saved in which directory ?')
    args = parser.parse_args()
    main(args)