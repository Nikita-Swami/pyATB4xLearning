#if we have not used this statis method then we want to inherit the class

class ExcelReader:

    @staticmethod
    def readExcelFile():
        print("Reading From Excel")

class TC1:
    def runTC(self):
        ExcelReader.readExcelFile()

tc1 = TC1()
tc1.runTC()