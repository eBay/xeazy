# *********************************************************
# Copyright 2018 eBay Inc.
# Developer : Karunamoorthy,Elango
# Architect : Gopalakrishnan Karunakaran,Jegan
#
# Use of this source code is governed by an MIT-style
# license that can be found in the LICENSE file or at
# https://opensource.org/licenses/MIT.
# *********************************************************

class Step(object):
    stepMessage = ''
    stepStartTime = ''
    steps = []
    screenShot = ''
    errorTrace = ''
    stepMessageStartingIndex = ''

    def __init__(self):
        self.stepMessage = ''
        self.stepStartTime = ''
        self.steps = []
        self.screenShot = ''
        self.errorTrace = ''
        self.stepMessageStartingIndex = ''

    def add_step_message(self, step_message):
        self.stepMessage = step_message

    def add_step_start_time(self, step_start_time):
        self.stepStartTime = str(step_start_time)+'s'

    def add_screen_shot(self, screen_shot):
        self.screenShot = screen_shot

    def add_steps(self, step):
        self.steps.append(step)

    def add_error_trace(self, error_trace):
        self.errorTrace = error_trace

    def add_stepMessageStartingIndex(self,inex):
        self.stepMessageStartingIndex=inex
