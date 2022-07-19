#Native
import os.path
import subprocess
import sys
import shutil
#Custom
from parse import Parser
from error import Error

class Interpreter:
    def Interpret(self, code : str) -> None:
        subprocess.call(["python", "output.py"])


def GetCode(filePath) -> str:
    if os.path.isfile(filePath):
        with open(filePath, 'r') as file:
            return file.read()
    else:
        Error("No se ha encontrado el archivo")

def HandleArgs() -> None:
    if sys.argv[1] == "--help" or sys.argv[1] == "-h":
        Error('''
        Command line arguments:
        --help -h: Escribe este mensaje
        --run -r (default) [file]: Inicializa el interprete a un archivo en especifico
            ''')
    elif sys.argv[1] == "--run" or sys.argv[1] == "-r":
        if len(sys.argv) < 3:
            Error("No coinciden los numeros de los argumentos")
        else:
            if os.path.isfile(sys.argv[2]):
                parser = Parser(GetCode((sys.argv[2])))
                interpreter = Interpreter()
                interpreter.Interpret(parser.code)
            else:
                Error("Archivo no encontrado")
    else:
        Error("El argumento es invalido")

    if (os.path.isfile("output.py")):
        os.remove("output.py")

def CheckArgs() -> str:
    if len(sys.argv) < 2:
        Error("Numero invalido de argumentos")
    HandleArgs()
    
if __name__ == "__main__":
    CheckArgs()
