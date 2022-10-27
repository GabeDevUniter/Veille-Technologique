# Generated from echo.g4 by ANTLR 4.11.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .echoParser import echoParser
else:
    from echoParser import echoParser

# This class defines a complete generic visitor for a parse tree produced by echoParser.

class echoVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by echoParser#prog.
    def visitProg(self, ctx:echoParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by echoParser#Variable.
    def visitVariable(self, ctx:echoParser.VariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by echoParser#Parent.
    def visitParent(self, ctx:echoParser.ParentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by echoParser#TypeExpr.
    def visitTypeExpr(self, ctx:echoParser.TypeExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by echoParser#OpExpr.
    def visitOpExpr(self, ctx:echoParser.OpExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by echoParser#IntType.
    def visitIntType(self, ctx:echoParser.IntTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by echoParser#FloatType.
    def visitFloatType(self, ctx:echoParser.FloatTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by echoParser#StringType.
    def visitStringType(self, ctx:echoParser.StringTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by echoParser#BoolType.
    def visitBoolType(self, ctx:echoParser.BoolTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by echoParser#TypeNeg.
    def visitTypeNeg(self, ctx:echoParser.TypeNegContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by echoParser#IntTypeNeg.
    def visitIntTypeNeg(self, ctx:echoParser.IntTypeNegContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by echoParser#FloatTypeNeg.
    def visitFloatTypeNeg(self, ctx:echoParser.FloatTypeNegContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by echoParser#decl.
    def visitDecl(self, ctx:echoParser.DeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by echoParser#assign_new.
    def visitAssign_new(self, ctx:echoParser.Assign_newContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by echoParser#assign.
    def visitAssign(self, ctx:echoParser.AssignContext):
        return self.visitChildren(ctx)



del echoParser