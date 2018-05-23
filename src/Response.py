# *********************************************************
# Copyright 2018 eBay Inc.
# Developer : Karunamoorthy,Elango
# Architect : Gopalakrishnan Karunakaran,Jegan
#
# Use of this source code is governed by an MIT-style
# license that can be found in the LICENSE file or at
# https://opensource.org/licenses/MIT.
# *********************************************************

class Response(object):
    overAllTests = ''
    numberOfPassedTests = ''
    numberOfFailedTests = ''
    suites = []
    sessionLogFilePath = ''
    deviceName = ''
    deviceOs = ''

    def __init__(self):
        self.overAllTests = ''
        self.numberOfPassedTests = ''
        self.numberOfFailedTests = ''
        self.testSuites = []
        self.sessionLogFilePath = ''
        self.deviceName = ''
        self.deviceOs = ''

    def add_overAllTests(self, overAll_Tests):
        self.overAllTests = overAll_Tests

    def add_numberOfPassedTests(self, numberOfPassed_Tests):
        self.numberOfPassedTests = numberOfPassed_Tests

    def add_numberOfFailedTests(self, numberOfFailed_Tests):
        self.numberOfFailedTests = numberOfFailed_Tests

    def add_testSuites(self, test_Suites):
        self.suites.append(test_Suites)

    def add_sessionLogFilePath(self, sessionLogFile_Path):
        self.sessionLogFilePath = sessionLogFile_Path

    def add_deviceName(self, device_Name):
        self.deviceName = device_Name

    def add_deviceOs(self, device_Os):
        self.deviceOs = device_Os