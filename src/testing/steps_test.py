# *********************************************************
# Copyright 2018 eBay Inc.
# Developer : Karunamoorthy,Elango
# Architect : Gopalakrishnan Karunakaran,Jegan
#
# Use of this source code is governed by an MIT-style
# license that can be found in the LICENSE file or at
# https://opensource.org/licenses/MIT.
# *********************************************************

import src.Xcprocessor as xc
s = ['    t =     0.01s     Set Up','    t =     0.03s         Launch com.ebay.iphone','    t =    10.14s         Find the /"webserver/" Other','    t =    10.15s             Snapshot accessibility hierarchy for com.ebay.iphone','    t =    15.47s     Tap "tab_search" Button','    t =    15.48s         Wait for app to idle']

x = xc.Xcprocessor()
listOfSteps = x.getTestSteps(s)
for steps in listOfSteps:
    print(steps)
    print('done')















