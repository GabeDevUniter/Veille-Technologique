import sys
from antlr4 import *
from echoLexer import echoLexer
from echoParser import echoParser
from echoVisitor import echoVisitor

EchoVersion = 0.1

if __name__ == "__main__":
    print(f'//------ Echo {EchoVersion} ------\\\\\n\n')
    while 1:
        shellInput = input('> ')
        if shellInput[-1] != ';': shellInput += ';'

        data = InputStream(shellInput)
        # lexer
        lexer = echoLexer(data)
        stream = CommonTokenStream(lexer)
        # parser
        parser = echoParser(stream)
        tree = parser.prog()
        # evaluator
        visitor = echoVisitor()

        try:
            output = visitor.visit(tree)
            if(output != None): print(output)
        except Exception as e:
            print(str(e))
