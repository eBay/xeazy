# *********************************************************
# Copyright 2018 eBay Inc.
# Developer : Karunamoorthy,Elango
# Architect : Gopalakrishnan Karunakaran,Jegan
#
# Use of this source code is governed by an MIT-style
# license that can be found in the LICENSE file or at
# https://opensource.org/licenses/MIT.
# *********************************************************

import traceback
import src.Response as rs
import src.TestSuite as ts
import src.TestCase as tc
import src.Step as steps

class Xcprocessor:

    def processXC(self, pipeData):
        testSuites = self.getAllTestSuites(pipeData)
        responseObj = self.getResponseObject(testSuites)
        responseObj.add_sessionLogFilePath(self.extract_session_log(pipeData))
        deviceName,OsVersion = self.setDeviceInfo(pipeData)
        responseObj.add_deviceName(deviceName)
        responseObj.add_deviceOs(OsVersion)
        return responseObj

    def getResponseObject(self,testSuites):
        response = rs.Response()
        overalltests = 0
        passesTests = 0
        failedTests = 0
        for suite in testSuites:
            print(suite.suiteName)
            for case in suite.testCases:
                print(case.methodName)
                print(case.result)
                if ('passed' in case.result):
                    passesTests += 1
                else:
                    failedTests +=1
        overalltests = passesTests + failedTests
        #setting up all required data for rendering
        response.add_testSuites(testSuites)
        response.add_overAllTests(overalltests)
        response.add_numberOfPassedTests(passesTests)
        response.add_numberOfFailedTests(failedTests)
        return response

    def getAllTestSuites(self, outputList):
        suites = []
        testSuiteInProgress = False
        startNumber = 0
        for i, line in enumerate(outputList):
            if ('Test Suite' in line) and ('started' in line) and ('Selected tests' not in line) and ('ebay-ui-tests.xctest' not in line):
                if testSuiteInProgress:
                    endNumber = i - 1
                    suites.append(self.getTestSuiteObject(outputList[startNumber:endNumber]))
                    testSuiteInProgress = True
                    startNumber = i
                else:
                    startNumber = i
                    testSuiteInProgress = True
            if ('Test Suite' in line) and (('passed' in line) or ('failed' in line)) and ('Selected tests' not in line) and ('ebay-ui-tests.xctest' not in line) :
                endNumber = i
                suites.append(self.getTestSuiteObject(outputList[startNumber:endNumber]))
                testSuiteInProgress = False
        if testSuiteInProgress:
            suites.append(self.getTestSuiteObject(outputList[startNumber:len(outputList)]))
        return suites

    def getTestSuiteObject(self, testSuiteData):
        testSuite = ts.TestSuite()
        stepData = []
        try:
            for i, line in enumerate(testSuiteData):
                if ('Test Case' in line) and ('started' in line):
                    testCase = tc.TestCase()
                    start = '['
                    end = ']'
                    testSuiteAndCaseName = self.find_between(line,start,end)
                    testSuiteAndCaseNames = testSuiteAndCaseName.split(" ")
                    testSuite.add_suite_name(testSuiteAndCaseNames[0])
                    testCase.add_method_name(testSuiteAndCaseNames[1])
                    testCase.add_event_type('started')
                if('fatal error' in line):
                    testCase.add_result('failed')
                    testCase.add_event_type('ended')
                    testCase.add_steps(self.getTestSteps(stepData))
                    testSuite.add_test_case(testCase)
                    stepData = []
                elif ('Test Case' in line) and ('passed' in line):
                    totalDuration = self.find_between(line,'(',')')
                    testCase.add_total_time_taken(totalDuration)
                    testCase.add_result('passed')
                    testCase.add_event_type('ended')
                    testCase.add_steps(self.getTestSteps(stepData))
                    testSuite.add_test_case(testCase)
                    stepData = []
                elif('Test Case' in line) and ('failed' in line):
                    totalDuration = self.find_between(line,"(",")")
                    testCase.add_total_time_taken(totalDuration)
                    testCase.add_result('failed')
                    testCase.add_event_type('ended')
                    testCase.add_steps(self.getTestSteps(stepData))
                    testSuite.add_test_case(testCase)
                    stepData = []
                if ('t =' in line):
                    stepData.append(line)

        except:
            traceback.print_exc()
        return testSuite

    def find_between(self,lineData,first,last):
        try:
            start = lineData.index( first ) + len( first )
            end = lineData.index( last, start )
            return lineData[start:end]
        except ValueError:
            return ""

    def find_between_r(self,lineData, first, last ):
        try:
            start = lineData.rindex( first ) + len( first )
            end = lineData.rindex( last, start )
            return lineData[start:end]
        except ValueError:
            return ""
    def maintainStack(self,stack,stepList):

        if(0 == stack.__len__()):
            testCase = tc.TestCase()
            dict = {stepList[0].stepMessageStartingIndex: testCase}
            stack.append(dict)
            return stack

        lastStackDic = stack[stack.__len__()-1]
        dicKey = ''
        for key in lastStackDic:
            dicKey = key
            break

        lastStepObj = stepList[stepList.__len__()-1]
        lastStepObj_stepMessageStartingIndex = lastStepObj.stepMessageStartingIndex

        if(dicKey == lastStepObj_stepMessageStartingIndex):
            return stack
        elif(dicKey < lastStepObj_stepMessageStartingIndex):
            dict = {stepList[stepList.__len__()-1].stepMessageStartingIndex: stepList[stepList.__len__()-2]}
            stack.append(dict)
            return stack
        elif(dicKey>lastStepObj_stepMessageStartingIndex):
            stack.pop()
            return self.maintainStack(stack,stepList)

    def addSteptoParent(self,step,stack):
        lastStackDic = stack[stack.__len__()-1]
        for key in lastStackDic:
            #print(key)
            stackTopStep = lastStackDic.get(key)
            stackTopStep.add_steps(step)
            break

    def getTestSteps(self,lineData):
        stepsDetails = []
        for line in lineData:
                duration = self.find_between(line,'=','s')
                stepMessage = line[line.index('s')+1:line.__len__()]
                for i, char in enumerate(stepMessage):
                    if (char.isspace()):
                        continue
                    else:
                        stepActualMessage = stepMessage[i:stepMessage.__len__()]
                        step = steps.Step()
                        step.add_step_message(stepActualMessage)
                        step.add_step_start_time(duration.strip())
                        step.add_stepMessageStartingIndex(i)
                        stepsDetails.append(step)
                        break
        stack = []
        for j,stepDetail in enumerate(stepsDetails):
            #print(str(stepDetail.stepMessage)+"|"+str(stepDetail.stepStartTime)+"|"+str(stepDetail.stepMessageStartingIndex))
            if(j != stepsDetails.__len__()):
                stepProcessingStep = stepsDetails[0:j+1]
                stack = self.maintainStack(stack,stepProcessingStep)
                self.addSteptoParent(stepDetail,stack)
        dictionaryStepData  = stack[0]
        for key in dictionaryStepData:
            #print(key)
            testCaseContainSteps = dictionaryStepData.get(key)
            return testCaseContainSteps.steps

    def extract_session_log(self,output):
        diag_msg = 'IDETestOperationsObserverDebug: Writing diagnostic log for test session to:'
        nextLine = False
        try:
            for lines in output:
                if(diag_msg in lines):
                  nextLine = True
                  continue
                if(nextLine):
                    print(lines)
                    return lines
                    break
        except:
            return "#"

    def setDeviceInfo(self,output):
        diag_msg = 'SimDevice'
        fullLineData = ''
        try:
            for lines in output:
                if(diag_msg in lines):
                  fullLineData = lines
                  break

            deviceName = self.find_between(fullLineData,':','(')
            osVersion = self.find_between(fullLineData,',',',')
            return deviceName,osVersion
        except:
            return ' ',' '

