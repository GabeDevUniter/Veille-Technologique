import sys
from antlr4 import *
from echoLexer import echoLexer
from echoParser import echoParser
from echoVisitorMain import echoVisitorMain

EchoVersion = '0.2 BETA'

if __name__ == "__main__":
    print(f'//------ Echo {EchoVersion} ------\\\\\n\n')
    while 1:
        shellInput = input('> ')
        if shellInput == 'exit' or shellInput == 'quit': break
        if shellInput[-1] != ';' and not shellInput.startswith(('if', 'elif', 'else', 'for', 'endfor', 'endif')): shellInput += ';'

        data = InputStream(shellInput)
        # lexer
        lexer = echoLexer(data)
        stream = CommonTokenStream(lexer)
        # parser
        parser = echoParser(stream)
        tree = parser.prog()
        # evaluator
        visitor = echoVisitorMain()

        # output = visitor.visit(tree)
        # if(output != None): print(output)
        try:
            # pass
            output = visitor.visit(tree)
            if(output != None): print(output)
        except Exception as e:
            print(str(e))
