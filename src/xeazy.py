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
import sys
import os
import shutil
import errno

def main(args):
    print(args.report)
    pipeData = []
    for line in sys.stdin:
        pipeData.append(line)

    x = xc.Xcprocessor()
    responseObj = x.processXC(pipeData)

    template_dir = resource_path('templates')
    env = Environment(
        loader=FileSystemLoader(template_dir)
    )
    template = env.get_template('template.html')
    output_from_parsed_template = template.render(suites=responseObj.suites, response=responseObj)
    with open(template_dir+"/dashboard.html", "wb") as fh:
        fh.write(output_from_parsed_template)


    #Creating out-put directory and copy/move files
    outputDirectory = args.output
    outputDirectoryPath = outputDirectory+"/xeazy-output/"
    print(outputDirectoryPath)
    try:
        os.makedirs(os.path.dirname(outputDirectoryPath))
    except OSError as exc: # Guard against race condition
        if exc.errno != errno.EEXIST:
            raise
    shutil.rmtree( outputDirectoryPath)
    shutil.copytree(template_dir+"/assets", outputDirectoryPath+"/assets")
    shutil.move(template_dir+"/dashboard.html", outputDirectoryPath+"/dashboard.html")
    #write to file for debug
    writeToFile(pipeData,outputDirectoryPath)

def resource_path(relative_path):
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

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