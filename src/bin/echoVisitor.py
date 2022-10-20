# Generated from echo.g4 by ANTLR 4.11.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .echoParser import echoParser
else:
    from echoParser import echoParser

# This class defines a complete generic visitor for a parse tree produced by echoParser.

class echoVisitor(ParseTreeVisitor):

    def visitProg(self, ctx:echoParser.ProgContext):
        decl = ctx.decl()
        expr = ctx.expr()

        if decl != []:
            self.visit(ctx.decl()[0])
            return None
        return self.visit(ctx.expr()[0])


    # Visit a parse tree produced by echoParser#Variable.
    def visitVariable(self, ctx:echoParser.VariableContext):
        #print(1)
        return self.visitChildren(ctx)


    # Visit a parse tree produced by echoParser#Parent.
    def visitParent(self, ctx:echoParser.ParentContext):
        #print(2)
        return self.visit(ctx.expr())


    # Visit a parse tree produced by echoParser#TypeExpr.
    def visitTypeExpr(self, ctx:echoParser.TypeExprContext):
        #print(3)
        return self.visit(ctx.value)


    # Visit a parse tree produced by echoParser#OpExpr.
    def visitOpExpr(self, ctx:echoParser.OpExprContext):
        #print(4)
        num1 = self.visit(ctx.left)
        num2 = self.visit(ctx.right)

        op = ctx.op.text

        if op == '+': return num1 + num2
        elif op == '-': return num1 - num2
        elif op == '*': return num1 * num2
        elif op == '/': return num1 / num2
        elif op == '**': return num1 ** num2
        return self.visitChildren(ctx)


    # Visit a parse tree produced by echoParser#IntType.
    def visitIntType(self, ctx:echoParser.IntTypeContext):
        #print(5)
        return int(ctx.getText())


    # Visit a parse tree produced by echoParser#FloatType.
    def visitFloatType(self, ctx:echoParser.FloatTypeContext):
        #print(6)
        return float(ctx.getText())


    # Visit a parse tree produced by echoParser#StringType.
    def visitStringType(self, ctx:echoParser.StringTypeContext):
        #print(7)
        return str(ctx.getText().replace('"', '').replace("'", ''))


    # Visit a parse tree produced by echoParser#TypeNeg.
    def visitTypeNeg(self, ctx:echoParser.TypeNegContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by echoParser#IntTypeNeg.
    def visitIntTypeNeg(self, ctx:echoParser.IntTypeNegContext):
        return int(ctx.getText())


    # Visit a parse tree produced by echoParser#FloatTypeNeg.
    def visitFloatTypeNeg(self, ctx:echoParser.FloatTypeNegContext):
        return float(ctx.getText())


    # Visit a parse tree produced by echoParser#decl.
    def visitDecl(self, ctx:echoParser.DeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by echoParser#assign.
    def visitAssign(self, ctx:echoParser.AssignContext):
        return self.visitChildren(ctx)



del echoParser
