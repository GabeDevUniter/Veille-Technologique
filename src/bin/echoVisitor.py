# Generated from echo.g4 by ANTLR 4.11.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .echoParser import echoParser
else:
    from echoParser import echoParser

# This class defines a complete generic visitor for a parse tree produced by echoParser.

class echoVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by echoParser#Float.
    def visitFloat(self, ctx:echoParser.FloatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by echoParser#Parent.
    def visitParent(self, ctx:echoParser.ParentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by echoParser#OpExpr.
    def visitOpExpr(self, ctx:echoParser.OpExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by echoParser#Int.
    def visitInt(self, ctx:echoParser.IntContext):
        return self.visitChildren(ctx)



del echoParser