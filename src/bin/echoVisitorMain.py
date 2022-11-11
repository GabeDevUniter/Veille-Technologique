# Generated from echo.g4 by ANTLR 4.11.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .echoParser import echoParser
else:
    from echoParser import echoParser

from echoVisitor import echoVisitor

from lib.EchoLib import *

class echoVisitorMain(echoVisitor):

    def ExecuteInstruction(self, ctx):
        decl = ctx.decl()
        expr = ctx.expr()
        block = ctx.block()

        if decl != []:
            self.visit(ctx.decl()[0])
            return None
        if block != []:
            self.visit(ctx.block()[0])
            return None
        return self.visit(ctx.expr()[0])

    # TODO : Support nested if statements where they're only executed when the root if block ends
    def ExecuteIfStatement(self, ifscope, ifscopeIndex):
        hasElif = 'elif' in ifscope
        hasElse = 'else' in ifscope

        cond = self.visit(ifscope[1].expr())

        if(cond):
            # if hasElif: del ifscope['elif']
            # elif hasElse: del ifscope['else']


            try:
                for ins in ifscope[0]:
                    self.ExecuteInstruction(ins)
            except Exception as e:
                raise
            finally:
                global currentScope
                while len(currentScope) != ifscopeIndex: PopScope()
                print('Scope is ' + str(currentScope))

        else:
            if hasElif: self.ExecuteIfStatement(ifscope['elif'], ifscopeIndex) # Recursive

            elif hasElse:
                try:
                    for ins in ifscope['else'][0]:
                        self.ExecuteInstruction(ins)

                except Exception as e:
                    raise
                finally:
                    while len(currentScope) != ifscopeIndex: PopScope()
                    print('Scope is ' + str(currentScope))


    def visitProg(self, ctx:echoParser.ProgContext):
        # print(currentScope)

        if currentScope[-1] == 'global' or ctx.block() != []:
            print('-- Regular Instruction')
            return self.ExecuteInstruction(ctx)
        else:
            print('-- Block Instruction')
            scope = GetCurrentScope()
            if 0 not in scope: scope[0] = []
            scope[0].append(ctx)

        return None
        # decl = ctx.decl()
        # expr = ctx.expr()
        # block = ctx.block()
        #
        # if decl != []:
        #     self.visit(ctx.decl()[0])
        #     return None
        # if block != []:
        #     self.visit(ctx.block()[0])
        #     return None
        # return self.visit(ctx.expr()[0])


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
        cond = self.visit(ctx.expr())

        if type(cond) != bool: raise Exception('IF statement must be a condition!')

        AddScope('if')

        GetCurrentScope()[1] = ctx

        return self.visitChildren(ctx)

    # Visit a parse tree produced by echoParser#ElifBlock.
    def visitElifBlock(self, ctx:echoParser.ElifBlockContext):
        print('#ElifBlock')

        if currentScope[-1] not in ['if', 'elif']: raise Exception('ELIF must succeed an IF or ELIF statement!')

        cond = self.visit(ctx.expr())
        if type(cond) != bool: raise Exception('IF statement must be a condition!')

        AddScope('elif')

        GetCurrentScope()[1] = ctx

        return self.visitChildren(ctx)


    # Visit a parse tree produced by echoParser#ElseBlock.
    def visitElseBlock(self, ctx:echoParser.ElseBlockContext):
        print('#ElseBlock')

        if currentScope[-1] not in ['if', 'elif']: raise Exception('ELSE must succeed an IF or ELIF statement!')

        AddScope('else')

        return self.visitChildren(ctx)

    # Visit a parse tree produced by echoParser#EndIfBlock.
    def visitEndIfBlock(self, ctx:echoParser.EndIfBlockContext):
        print('#EndIfBlock')

        # Get the last index of 'if' in negative value
        #ifscopeIndex = currentScope[::-1].index('if') * -1 - 1

        # Last index of if
        ifscopeIndex = len(currentScope) - currentScope[::-1].index('if') - 1

        if currentScope[-1] not in ['if', 'elif', 'else']: raise Exception('ENDIF must  succeed an IF, ELIF or ELSE statement')

        try:
            ifscope = GetScopeAt(ifscopeIndex)

            self.ExecuteIfStatement(ifscope, ifscopeIndex)
            print(currentScope)
            # hasElif = 'elif' in ifscope
            # hasElse = 'else' in ifscope
            #
            # cond = self.visit(ifscope[1].ctx.expr())
            #
            # if(cond):
            #     if hasElif: del ifscope['elif']
            #     if hasElse: del ifscope['else']
            #     currentScope = currentScope[:ifscopeIndex + 1]
            #
            #     for ins in GetCurrentScope()[0]:
            #         self.ExecuteInstruction(ins)
        except Exception as e:
            raise
        finally:
            pass
            #print('About to pop scope')

            #PopScope();

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
            #print((type,var,value))

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

        # if not IsDefined(var):
        if varValue == None:
            #print(varValue)
            return self.visitChildren(ctx)

        if assign_op == '=': AssignVariable(var, value)
        elif assign_op == '+=': AssignVariable(var, varValue + value)
        elif assign_op == '-=': AssignVariable(var, varValue - value)
        elif assign_op == '*=': AssignVariable(var, varValue * value)
        elif assign_op == '/=': AssignVariable(var, varValue / value)
        elif assign_op == '**=': AssignVariable(var, varValue ** value)

        #print(GetVariable(var))

        return self.visitChildren(ctx)


    # Visit a parse tree produced by echoParser#AssignInc.
    def visitAssignInc(self, ctx:echoParser.AssignIncContext):
        print('#AssignInc')

        var = ctx.VAR().getText()
        varValue = GetVariable(var)

        if not IsDefined(var):
            #print(varValue)
            return self.visitChildren(ctx)

        AssignVariable(var, varValue + 1)

        return self.visitChildren(ctx)


    # Visit a parse tree produced by echoParser#AssignDec.
    def visitAssignDec(self, ctx:echoParser.AssignDecContext):
        print('#AssignDec')

        var = ctx.VAR().getText()
        varValue = GetVariable(var)

        if not IsDefined(var):
            #print(varValue)
            return self.visitChildren(ctx)

        AssignVariable(var, varValue - 1)

        return self.visitChildren(ctx)

del echoParser
