import sys
from antlr4 import *
from echoLexer import echoLexer
from echoParser import echoParser
from echoVisitorMain import echoVisitorMain

EchoVersion = '0.2 ALPHA'

if __name__ == "__main__":
    print(f'//------ Echo {EchoVersion} ------\\\\\n\n')
    while 1:
        shellInput = input('> ')
        if shellInput == 'exit' or shellInput == 'quit': break
        if shellInput[-1] != ';': shellInput += ';'

        data = InputStream(shellInput)
        # lexer
        lexer = echoLexer(data)
        stream = CommonTokenStream(lexer)
        # parser
        parser = echoParser(stream)
        tree = parser.prog()
        # evaluator
        visitor = echoVisitorMain()

        try:
            output = visitor.visit(tree)
            if(output != None): print(output)
        except Exception as e:
            print(str(e))
