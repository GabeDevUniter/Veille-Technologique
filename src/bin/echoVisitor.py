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


    # Visit a parse tree produced by echoParser#FuncCall.
    def visitFuncCall(self, ctx:echoParser.FuncCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by echoParser#Variable.
    def visitVariable(self, ctx:echoParser.VariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by echoParser#Parent.
    def visitParent(self, ctx:echoParser.ParentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by echoParser#CompExpr.
    def visitCompExpr(self, ctx:echoParser.CompExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by echoParser#CompLogic.
    def visitCompLogic(self, ctx:echoParser.CompLogicContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by echoParser#TypeExpr.
    def visitTypeExpr(self, ctx:echoParser.TypeExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by echoParser#OpExpr.
    def visitOpExpr(self, ctx:echoParser.OpExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by echoParser#FuncReturn.
    def visitFuncReturn(self, ctx:echoParser.FuncReturnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by echoParser#IfBlock.
    def visitIfBlock(self, ctx:echoParser.IfBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by echoParser#ElifBlock.
    def visitElifBlock(self, ctx:echoParser.ElifBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by echoParser#ElseBlock.
    def visitElseBlock(self, ctx:echoParser.ElseBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by echoParser#EndIfBlock.
    def visitEndIfBlock(self, ctx:echoParser.EndIfBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by echoParser#ForBlock.
    def visitForBlock(self, ctx:echoParser.ForBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by echoParser#ForStepBlock.
    def visitForStepBlock(self, ctx:echoParser.ForStepBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by echoParser#EndForBlock.
    def visitEndForBlock(self, ctx:echoParser.EndForBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by echoParser#FunctionBlock.
    def visitFunctionBlock(self, ctx:echoParser.FunctionBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by echoParser#EndFunctionBlock.
    def visitEndFunctionBlock(self, ctx:echoParser.EndFunctionBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by echoParser#NumType.
    def visitNumType(self, ctx:echoParser.NumTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by echoParser#StringType.
    def visitStringType(self, ctx:echoParser.StringTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by echoParser#BoolType.
    def visitBoolType(self, ctx:echoParser.BoolTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by echoParser#IntType.
    def visitIntType(self, ctx:echoParser.IntTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by echoParser#FloatType.
    def visitFloatType(self, ctx:echoParser.FloatTypeContext):
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


    # Visit a parse tree produced by echoParser#AssignRegular.
    def visitAssignRegular(self, ctx:echoParser.AssignRegularContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by echoParser#AssignInc.
    def visitAssignInc(self, ctx:echoParser.AssignIncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by echoParser#AssignDec.
    def visitAssignDec(self, ctx:echoParser.AssignDecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by echoParser#assign_op.
    def visitAssign_op(self, ctx:echoParser.Assign_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by echoParser#func.
    def visitFunc(self, ctx:echoParser.FuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by echoParser#return.
    def visitReturn(self, ctx:echoParser.ReturnContext):
        return self.visitChildren(ctx)



del echoParser