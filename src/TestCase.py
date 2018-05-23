# *********************************************************
# Copyright 2018 eBay Inc.
# Developer : Karunamoorthy,Elango
# Architect : Gopalakrishnan Karunakaran,Jegan
#
# Use of this source code is governed by an MIT-style
# license that can be found in the LICENSE file or at
# https://opensource.org/licenses/MIT.
# *********************************************************

class TestCase(object):
    className = ''
    methodName = ''
    eventType = ''
    steps = []
    totalTimeTaken = ''
    result = ''

    def __init__(self):
        self.className = ''
        self.methodName = ''
        self.eventType = ''
        self.steps = []
        self.totalTimeTaken = ''
        self.result = ''

    def add_class_name(self, class_name):
        self.className = class_name

    def add_method_name(self, method_name):
        self.methodName = method_name

    def add_event_type(self, event_type):
        self.eventType = event_type

    def add_steps(self, step):
        self.steps.append(step)

    def add_total_time_taken(self, time_taken):
        self.totalTimeTaken = time_taken

    def add_result(self, _result):
        self.result = _result
