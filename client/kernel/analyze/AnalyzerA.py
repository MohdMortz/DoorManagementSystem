class AnalyzerA(object):

    uc_Buffer_PRG = 0

    ####################################################################################################
    def __init__(self):
        ""

    ####################################################################################################
    def getParamNo(self):
        raise NotImplementedError("Please Implement this method")

    ####################################################################################################
    def analyze(self, dataList):
        raise NotImplementedError("Please Implement this method")

    ####################################################################################################
    def isValid(self):
        return True

    ####################################################################################################
    def setValid(self, valid):
        ""

    ####################################################################################################
    def checkForValidity(self):
        return True