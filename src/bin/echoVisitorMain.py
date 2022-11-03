# Generated from echo.g4 by ANTLR 4.11.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .echoParser import echoParser
else:
    from echoParser import echoParser

from echoVisitor import echoVisitor

from lib.EchoLib import *

class echoVisitorMain(echoVisitor):

    def visitProg(self, ctx:echoParser.ProgContext):
        decl = ctx.decl()
        expr = ctx.expr()

        if decl != []:
            self.visit(ctx.decl()[0])
            return None
        return self.visit(ctx.expr()[0])


    # Visit a parse tree produced by echoParser#Variable.
    def visitVariable(self, ctx:echoParser.VariableContext):
        # print('#Variable')
        return GetVariable(ctx.getText())


    # Visit a parse tree produced by echoParser#Parent.
    def visitParent(self, ctx:echoParser.ParentContext):
        # print('#Parent')
        return self.visit(ctx.expr())


    # Visit a parse tree produced by echoParser#TypeExpr.
    def visitTypeExpr(self, ctx:echoParser.TypeExprContext):
        # print('#typeExpr')
        return self.visitChildren(ctx)


    # Visit a parse tree produced by echoParser#OpExpr.
    def visitOpExpr(self, ctx:echoParser.OpExprContext):
        # print('#OpExpr')
        num1 = self.visit(ctx.left)
        num2 = self.visit(ctx.right)

        op = ctx.op.text

        if op == '+': return num1 + num2
        elif op == '-': return num1 - num2
        elif op == '*': return num1 * num2
        elif op == '/': return num1 / num2
        elif op == '**': return num1 ** num2
        elif op == '<<': return num1 << num2
        elif op == '>>': return num1 >> num2
        return self.visitChildren(ctx)

    # Visit a parse tree produced by echoParser#IfBlock.
    def visitIfBlock(self, ctx:echoParser.IfBlockContext):
        print('#IfBlock')
        return self.visitChildren(ctx)


    # Visit a parse tree produced by echoParser#EndIfBlock.
    def visitEndIfBlock(self, ctx:echoParser.EndIfBlockContext):
        print('#EndIfBlock')
        return self.visitChildren(ctx)


    # Visit a parse tree produced by echoParser#ForBlock.
    def visitForBlock(self, ctx:echoParser.ForBlockContext):
        print('#ForBlock')
        return self.visitChildren(ctx)


    # Visit a parse tree produced by echoParser#ForNextBlock.
    def visitForNextBlock(self, ctx:echoParser.ForNextBlockContext):
        print('#ForNextBlock')
        return self.visitChildren(ctx)


    # Visit a parse tree produced by echoParser#EndForBlock.
    def visitEndForBlock(self, ctx:echoParser.EndForBlockContext):
        print('#EndForBlock')
        return self.visitChildren(ctx)

    # Visit a parse tree produced by echoParser#CompExpr.
    def visitCompExpr(self, ctx:echoParser.CompExprContext):
        # print('#CompExpr')

        expr1 = self.visit(ctx.left)
        expr2 = self.visit(ctx.right)

        op = ctx.op.text

        # print(op)

        if op == '==': return expr1 == expr2
        elif op == '<': return expr1 < expr2
        elif op == '<=': return expr1 <= expr2
        elif op == '>': return expr1 > expr2
        elif op == '>=': return expr1 >= expr2
        elif op == '!=': return expr1 != expr2
        return self.visitChildren(ctx)


    # Visit a parse tree produced by echoParser#CompLogic.
    def visitCompLogic(self, ctx:echoParser.CompLogicContext):
        # print('#CompLogic')
        return self.visitChildren(ctx)

    # Visit a parse tree produced by echoParser#IntType.
    def visitIntType(self, ctx:echoParser.IntTypeContext):
        #print('#IntType')
        return int(ctx.getText())


    # Visit a parse tree produced by echoParser#FloatType.
    def visitFloatType(self, ctx:echoParser.FloatTypeContext):
        #print('#FloatType')
        return float(ctx.getText())


    # Visit a parse tree produced by echoParser#StringType.
    def visitStringType(self, ctx:echoParser.StringTypeContext):
        #print('#StringType')
        return str(ctx.getText().replace('"', '').replace("'", ''))

    # Visit a parse tree produced by echoParser#BoolType.
    def visitBoolType(self, ctx:echoParser.BoolTypeContext):
        #print('#BoolType')
        return bool(ctx.getText())

    # Visit a parse tree produced by echoParser#TypeNeg.
    def visitTypeNeg(self, ctx:echoParser.TypeNegContext):
        #print('#TypeNeg')
        return self.visitChildren(ctx)


    # Visit a parse tree produced by echoParser#IntTypeNeg.
    def visitIntTypeNeg(self, ctx:echoParser.IntTypeNegContext):
        #print('#IntTypeNeg')
        return int(ctx.getText())


    # Visit a parse tree produced by echoParser#FloatTypeNeg.
    def visitFloatTypeNeg(self, ctx:echoParser.FloatTypeNegContext):
        #print('#FloatTypeNeg')
        return float(ctx.getText())


    # Visit a parse tree produced by echoParser#decl.
    def visitDecl(self, ctx:echoParser.DeclContext):
        # print('#Decl')

        try:
            var = ctx.assign_new().VAR().getText()
            value = self.visit(ctx.assign_new().expr())
            type = ctx.TYPE_NAME().getText()
            print((type,var,value))

            #print('DeclareVariable()')
            DeclareVariable(type, var, value)
        except:

            #print('AssignVariable()')
            #var = ctx.assign().VAR().getText()
            #value = self.visit(ctx.assign().expr())
            #AssignVariable(var, value)
            return self.visit(ctx.assign())

        return self.visitChildren(ctx)

    # Visit a parse tree produced by echoParser#assign_new.
    def visitAssign_new(self, ctx:echoParser.Assign_newContext):
        #print('#Assign_new')
        return self.visitChildren(ctx)

    # Visit a parse tree produced by echoParser#AssignRegular.
    def visitAssignRegular(self, ctx:echoParser.AssignRegularContext):
        #print('#AssignRegular')

        var = ctx.VAR().getText()
        assign_op = ctx.assign_op().getText()
        value = self.visit(ctx.expr())
        varValue = GetVariable(var)

        if not IsDefined(var):
            print(varValue)
            return self.visitChildren(ctx)

        if assign_op == '=': AssignVariable(var, value)
        elif assign_op == '+=': AssignVariable(var, varValue + value)
        elif assign_op == '-=': AssignVariable(var, varValue - value)
        elif assign_op == '*=': AssignVariable(var, varValue * value)
        elif assign_op == '/=': AssignVariable(var, varValue / value)
        elif assign_op == '**=': AssignVariable(var, varValue ** value)

        return self.visitChildren(ctx)


    # Visit a parse tree produced by echoParser#AssignInc.
    def visitAssignInc(self, ctx:echoParser.AssignIncContext):
        print('#AssignInc')

        var = ctx.VAR().getText()
        varValue = GetVariable(var)

        if not IsDefined(var):
            print(varValue)
            return self.visitChildren(ctx)

        AssignVariable(var, varValue + 1)

        return self.visitChildren(ctx)


    # Visit a parse tree produced by echoParser#AssignDec.
    def visitAssignDec(self, ctx:echoParser.AssignDecContext):
        print('#AssignDec')

        var = ctx.VAR().getText()
        varValue = GetVariable(var)

        if not IsDefined(var):
            print(varValue)
            return self.visitChildren(ctx)

        AssignVariable(var, varValue - 1)

        return self.visitChildren(ctx)

del echoParser
