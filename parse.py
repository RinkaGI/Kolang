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
        code = self.ParseVariables(code)
        code = self.ParseConverting(code)
        code = self.ParseInputFunction(code)
        code = self.ParseConditional(code)

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

    # Print function
    def ParsePrintFunction(self, code: str) -> str:
        for line in code.splitlines():
            if "ESCRIBIR " in line:
                if not self.IsInString("ESCRIBIR ", line):
                    comando = line
                    newLine = comando.replace("ESCRIBIR ", "print(")
                    code = code.replace(line, newLine + ")")
        return code

    # Variables
    def ParseVariables(self, code: str) -> str:
        for line in code.splitlines():
            if "VAR " in line:
                if not self.IsInString("VAR ", line):
                    comando = line
                    newLine = comando.replace("VAR ", "")
                    code = code.replace(line, newLine)

        return code

    def ParseConverting(self, code: str) -> str:
        for line in code.splitlines():
            if "CONVERTIR-A-TEXTO " in line:
                if not self.IsInString("CONVERTIR-A-TEXTO ", line):
                    comando = line
                    newLine = comando.replace("CONVERTIR-A-TEXTO ", "str(")
                    code = code.replace(line, newLine + ")")
            
            if "CONVERTIR-A-ENTERO " in line:
                if not self.IsInString("CONVERTIR-A-ENTERO ", line):
                    comando = line
                    newLine = comando.replace("CONVERTIR-A-ENTERO ", "int(")
                    code = code.replace(line, newLine + ")")

        return code

    # Input function
    def ParseInputFunction(self, code: str) -> str:
        for line in code.splitlines():
            if "RECIBIR " in line:
                if not self.IsInString("RECIBIR ", line):
                    comando = line
                    newLine = comando.replace("RECIBIR ", "input(")
                    code = code.replace(line, newLine + ")")

        return code

    # Condicionales (desearme suerte)
    def ParseConditional(self, code: str) ->  str:
        for line in code.splitlines():
            if "SI " in line:
                if not self.IsInString("SI ", line):
                    comando = line
                    newLine = comando.replace("SI ", "if ")
                    code = code.replace(line, newLine)
            if "O " in line:
                if not self.IsInString("O ", line):
                    comando = line
                    newLine = comando.replace("O ", "elif ")
                    code = code.replace(line, newLine)
            if "OTRA_COSA" in line:
                if not self.IsInString("OTRA_COSA", line):
                    comando = line
                    newLine = comando.replace("OTRA_COSA", "else")
                    code = code.replace(line, newLine)

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
