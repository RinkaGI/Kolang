from error import Error

class Parser:
    def __init__(self, code: str):
        #Pass in code
        self.code = code
        #Parse code
        self.code = self.Parse(self.code)

    def Parse(self, code: str) -> str:
        #Parse code into normal python
        code = self.ParseComments(code)
        code = self.ParsePrintFunction(code)

        #Dump code to file
        with open("output.py", "w") as f:
            f.write(code)
        return code
     
    def ParseComments(self, code: str) -> str:
        for line in code.splitlines():
            if "//" in line:
                if not self.IsInString("//", line):
                    if list(line)[0] == "/" and list(line)[1] == "/":
                        code = code.replace(line, "")
                    else:
                        newLine = line.partition("//")[0]
                        code = code.replace(line, newLine)                    
        return code

    def ParsePrintFunction(self, code: str) -> str:
        for line in code.splitlines():
            if "ESCRIBIR " in line:
                if not self.IsInString("ESCRIBIR ", line):
                    comando = line
                    newLine = comando.replace("ESCRIBIR ", "print(")
                    code = code.replace(line, newLine + ")")
        return code


    def IsInString(self, phrase : str, line : str, returnIfMultiple = False) -> bool:
        if not phrase in line:
            return False
        if line.count(phrase) > 1:
            return returnIfMultiple
        leftSide = line.partition(phrase)[0]
        if leftSide.count("\"") > 0:
            if leftSide.count("\"") % 2 == 0:
                return False
            else:
                return True
        if leftSide.count("\'") > 0:
            if leftSide.count("\'") % 2 == 0:
                return False
            else:
                return True
