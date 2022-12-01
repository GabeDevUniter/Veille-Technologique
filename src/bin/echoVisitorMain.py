# Generated from echo.g4 by ANTLR 4.11.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .echoParser import echoParser
else:
    from echoParser import echoParser

from echoVisitor import echoVisitor

from lib.EchoLib import *
from lib.EchoClasses import *

class echoVisitorMain(echoVisitor):

    # +++++++++++++++++++++++++++++++++++++++
    # ++++---- INSTRUCTION EXECUTION ----++++
    # +++++++++++++++++++++++++++++++++++++++

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

    def ExecuteBlockInstructions(self, list):
        print('Executing Block')
        for ins in list:
            if type(ins) == dict:
                if 'if' in ins: self.ExecuteIfStatement(ins['if'], ins['if'][2])
                if 'for' in ins: self.ExecuteForStatement(ins['for'], ins['for'][4])

            else:
                self.ExecuteInstruction(ins)

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




    # ++++++++++++++++++++++++++++++
    # ++++---- IF STATEMENT ----++++
    # ++++++++++++++++++++++++++++++

    # TODO : Support nested if statements where they're only executed when the root if block ends
    def ExecuteIfStatement(self, ifscope, ifscopeIndex):
        hasElif = 'elif' in ifscope
        hasElse = 'else' in ifscope

        cond = self.visit(ifscope[1].expr())

        if(cond):
            # if hasElif: del ifscope['elif']
            # elif hasElse: del ifscope['else']


            try:
                self.ExecuteBlockInstructions(ifscope[0])
                # for ins in ifscope[0]:
                #     self.ExecuteInstruction(ins)
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
                    self.ExecuteBlockInstructions(ifscope['else'][0])
                    # for ins in ifscope['else'][0]:
                    #     self.ExecuteInstruction(ins)

                except Exception as e:
                    raise
                finally:
                    while len(currentScope) != ifscopeIndex: PopScope()
                    print('Scope is ' + str(currentScope))
            else:
                while len(currentScope) != ifscopeIndex: PopScope()

    # Visit a parse tree produced by echoParser#IfBlock.
    def visitIfBlock(self, ctx:echoParser.IfBlockContext):
        print('#IfBlock')

        # if type(cond) != bool: raise Exception('IF statement must be a condition!')
        if type(ctx.expr()).__name__ != 'CompExprContext': raise Exception('IF statement must be a condition!')

        AddScope('if')

        # GetCurrentScope()[0] = []
        GetCurrentScope()[1] = ctx

        #return self.visitChildren(ctx)
        return None

    # Visit a parse tree produced by echoParser#ElifBlock.
    def visitElifBlock(self, ctx:echoParser.ElifBlockContext):
        print('#ElifBlock')

        if currentScope[-1] not in ['if', 'elif']: raise Exception('ELIF must succeed an IF or ELIF statement!')

        # cond = self.visit(ctx.expr())
        # if type(cond) != bool: raise Exception('IF statement must be a condition!')
        if type(ctx.expr()).__name__ != 'CompExprContext': raise Exception('IF statement must be a condition!')

        AddScope('elif')

        # GetCurrentScope()[0] = []
        GetCurrentScope()[1] = ctx

        # return self.visitChildren(ctx)
        return None


    # Visit a parse tree produced by echoParser#ElseBlock.
    def visitElseBlock(self, ctx:echoParser.ElseBlockContext):
        print('#ElseBlock')

        if currentScope[-1] not in ['if', 'elif']: raise Exception('ELSE must succeed an IF or ELIF statement!')

        AddScope('else')

        # GetCurrentScope()[0] = []

        # return self.visitChildren(ctx)
        return None

    # Visit a parse tree produced by echoParser#EndIfBlock.
    def visitEndIfBlock(self, ctx:echoParser.EndIfBlockContext):
        print('#EndIfBlock')

        # Get the last index of 'if' in negative value
        #ifscopeIndex = currentScope[::-1].index('if') * -1 - 1

        # Last index of if
        ifscopeIndex = len(currentScope) - currentScope[::-1].index('if') - 1

        if currentScope[-1] not in ['if', 'elif', 'else']: raise Exception('ENDIF must  succeed an IF, ELIF or ELSE statement')

        print('Scope is ' + str(currentScope))

        try:
            ifscope = GetScopeAt(ifscopeIndex)

            ifscope[2] = ifscopeIndex

            print(ifscopeIndex)
            print(currentScope.index('if'))
            # if ifscopeIndex == currentScope.index('if'): self.ExecuteIfStatement(ifscope, ifscopeIndex)
            if ifscopeIndex == 1: self.ExecuteIfStatement(ifscope, ifscopeIndex)
            else:

                #TODO Nested if statements aren't correctly functioning with an elif. Fix it
                previousScope = GetScopeAt(ifscopeIndex-1)
                previousScope[0].append({'if':ifscope})
                print(previousScope)

                while len(currentScope) != ifscopeIndex: PopScope()



                print(previousScope)
                #print("\n".join("{}\t{}".format(k, v) for k, v in previousScope.items()))

                print('Scope is ' + str(currentScope))
                print(GetCurrentScope())

                # print(previousIfscope)

        except Exception as e:
            print(str(e))
        finally:
            pass
            #print('About to pop scope')

            #PopScope();

        return self.visitChildren(ctx)

    # ++++++++++++++++++++++++++
    # ++++---- FOR LOOP ----++++
    # ++++++++++++++++++++++++++

    def ExecuteForStatement(self, forscope, forscopeIndex):
        iter = forscope[forscope[1]][1]
        max = forscope[2]
        step = forscope[3]

        print((iter,max,step))

        if (step > 0 and iter < max) or (step < 0 and iter > max):
            self.ExecuteBlockInstructions(forscope[0])

            AssignVariable(forscope[1], iter + step)

            self.ExecuteForStatement(forscope, forscopeIndex)
        else:
            while len(currentScope) != forscopeIndex: PopScope()

    # TODO : Replace NEXT keyword with STEP for next parser compile

    # TODO : Support IF statements inside FOR loops (Works for a single IF block)

    def prepareForBlock(self, ctx, step=1):
        var = ctx.iter_.VAR().getText()
        value = self.visit(ctx.iter_.expr())
        max = self.visit(ctx.max_)
        type = 'int'

        AddScope('for')

        try:
            DeclareVariable(type, var, value)
        except Exception as e:
            PopScope()
            raise Exception('Iteration value must be a number!')

        forscope = GetCurrentScope()

        forscope[1] = var

        try:
            forscope[2] = int(max)
        except TypeError as e:
            PopScope()
            raise Exception('Final value must be a number!')

        # Step
        forscope[3] = step


        return self.visitChildren(ctx)

    # Visit a parse tree produced by echoParser#ForBlock.
    def visitForBlock(self, ctx:echoParser.ForBlockContext):
        print('#ForBlock')
        return self.prepareForBlock(ctx)

    # Visit a parse tree produced by echoParser#ForNextBlock.
    def visitForNextBlock(self, ctx:echoParser.ForNextBlockContext):
        print('#ForNextBlock')
        return self.prepareForBlock(ctx, self.visit(ctx.next_))


    # Visit a parse tree produced by echoParser#EndForBlock.
    def visitEndForBlock(self, ctx:echoParser.EndForBlockContext):
        print('#EndForBlock')

        if currentScope[-1] != 'for': raise Exception('ENDFOR must succeed a FOR statement')

        # Last index of for
        forscopeIndex = len(currentScope) - currentScope[::-1].index('for') - 1

        forscope = GetScopeAt(forscopeIndex)
        forscope[4] = forscopeIndex

        if forscopeIndex == 1: self.ExecuteForStatement(forscope, forscopeIndex)
        else:
            previousScope = GetScopeAt(forscopeIndex-1)
            previousScope[0].append({'for':forscope})
            print(previousScope)

            while len(currentScope) != forscopeIndex: PopScope()

        #self.ExecuteForStatement(GetScopeAt(forscopeIndex), forscopeIndex)

        return self.visitChildren(ctx)

    # ++++++++++++++++++++++++++++
    # +++++---- FUNCTION ----+++++
    # ++++++++++++++++++++++++++++

    # Visit a parse tree produced by echoParser#FunctionBlock.
    def visitFunctionBlock(self, ctx:echoParser.FunctionBlockContext):
        print('#FunctionBlock')

        AddScope('func')

    # Visit a parse tree produced by echoParser#EndFunctionBlock.
    def visitEndFunctionBlock(self, ctx:echoParser.EndFunctionBlockContext):
        print('#EndFunctionBlock')
        return self.visitChildren(ctx)

    # Visit a parse tree produced by echoParser#func.
    def visitFunc(self, ctx:echoParser.FuncContext):
        print('#FuncBlock')
        return self.visitChildren(ctx)


    # Visit a parse tree produced by echoParser#return.
    def visitReturn(self, ctx:echoParser.ReturnContext):
        print('#ReturnBlock')
        return self.visitChildren(ctx)

    # ++++++++++++++++++++++++++++
    # ++++---- EXPRESSION ----++++
    # ++++++++++++++++++++++++++++

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
        #print('#Decl')

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
