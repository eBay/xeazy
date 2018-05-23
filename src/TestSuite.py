# *********************************************************
# Copyright 2018 eBay Inc.
# Developer : Karunamoorthy,Elango
# Architect : Gopalakrishnan Karunakaran,Jegan
#
# Use of this source code is governed by an MIT-style
# license that can be found in the LICENSE file or at
# https://opensource.org/licenses/MIT.
# *********************************************************

class TestSuite(object):
    suiteName = ''
    eventType = ''
    suiteNames = []
    startTimestamp = ''
    endTimestamp = ''
    testCases = []
    totalTimeTaken = ''

    def __init__(self):
        self.suiteName = ''
        self.eventType = ''
        self.suiteNames = []
        self.startTimestamp = ''
        self.endTimestamp = ''
        self.testCases = []
        self.totalTimeTaken = ''

    def add_suite_name(self, suite_name):
        self.suiteName = suite_name

    def add_event_type(self, event_type):
        self.eventType = event_type

    def add_suite_names(self, suite_names):
        self.suiteNames.append(suite_names)

    def add_start_timestamp(self, start_timestamp):
        self.startTimestamp = start_timestamp

    def add_end_timestamp(self, end_timestamp):
        self.endTimestamp = end_timestamp

    def add_test_case(self, test_case):
        self.testCases.append(test_case)

    def add_total_time_taken(self, time_taken):
        self.totalTimeTaken = time_taken
