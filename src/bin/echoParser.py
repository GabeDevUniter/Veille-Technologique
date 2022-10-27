# Generated from echo.g4 by ANTLR 4.11.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,22,77,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,1,0,1,0,3,0,17,8,0,1,0,1,0,4,0,21,8,0,11,0,12,0,22,1,0,1,0,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,3,1,34,8,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,5,1,45,8,1,10,1,12,1,48,9,1,1,2,1,2,1,2,1,2,1,2,3,2,55,8,2,
        1,3,1,3,1,3,1,3,3,3,61,8,3,1,4,1,4,1,4,1,4,3,4,67,8,4,1,5,1,5,1,
        5,1,5,1,6,1,6,1,6,1,6,1,6,0,1,2,7,0,2,4,6,8,10,12,0,3,1,0,2,4,1,
        0,5,6,1,0,7,8,82,0,20,1,0,0,0,2,33,1,0,0,0,4,54,1,0,0,0,6,60,1,0,
        0,0,8,66,1,0,0,0,10,68,1,0,0,0,12,72,1,0,0,0,14,17,3,8,4,0,15,17,
        3,2,1,0,16,14,1,0,0,0,16,15,1,0,0,0,17,18,1,0,0,0,18,19,5,1,0,0,
        19,21,1,0,0,0,20,16,1,0,0,0,21,22,1,0,0,0,22,20,1,0,0,0,22,23,1,
        0,0,0,23,24,1,0,0,0,24,25,5,0,0,1,25,1,1,0,0,0,26,27,6,1,-1,0,27,
        34,5,14,0,0,28,34,3,4,2,0,29,30,5,9,0,0,30,31,3,2,1,0,31,32,5,10,
        0,0,32,34,1,0,0,0,33,26,1,0,0,0,33,28,1,0,0,0,33,29,1,0,0,0,34,46,
        1,0,0,0,35,36,10,5,0,0,36,37,7,0,0,0,37,45,3,2,1,6,38,39,10,4,0,
        0,39,40,7,1,0,0,40,45,3,2,1,5,41,42,10,2,0,0,42,43,7,2,0,0,43,45,
        3,2,1,3,44,35,1,0,0,0,44,38,1,0,0,0,44,41,1,0,0,0,45,48,1,0,0,0,
        46,44,1,0,0,0,46,47,1,0,0,0,47,3,1,0,0,0,48,46,1,0,0,0,49,55,5,15,
        0,0,50,55,5,16,0,0,51,55,5,17,0,0,52,55,5,18,0,0,53,55,3,6,3,0,54,
        49,1,0,0,0,54,50,1,0,0,0,54,51,1,0,0,0,54,52,1,0,0,0,54,53,1,0,0,
        0,55,5,1,0,0,0,56,57,5,6,0,0,57,61,5,15,0,0,58,59,5,6,0,0,59,61,
        5,16,0,0,60,56,1,0,0,0,60,58,1,0,0,0,61,7,1,0,0,0,62,63,5,13,0,0,
        63,64,5,11,0,0,64,67,3,10,5,0,65,67,3,12,6,0,66,62,1,0,0,0,66,65,
        1,0,0,0,67,9,1,0,0,0,68,69,5,14,0,0,69,70,5,12,0,0,70,71,3,2,1,0,
        71,11,1,0,0,0,72,73,5,14,0,0,73,74,5,12,0,0,74,75,3,2,1,0,75,13,
        1,0,0,0,8,16,22,33,44,46,54,60,66
    ]

class echoParser ( Parser ):

    grammarFileName = "echo.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "';'", "'*'", "'/'", "'**'", "'+'", "'-'", 
                     "'<<'", "'>>'", "'('", "')'", "':'", "'='" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "TYPE_NAME", "VAR", "INT", "FLOAT", "STRING", 
                      "BOOL", "COMMENT", "MULTICOMMENT", "NEWLINE", "WS" ]

    RULE_prog = 0
    RULE_expr = 1
    RULE_type = 2
    RULE_type_neg = 3
    RULE_decl = 4
    RULE_assign_new = 5
    RULE_assign = 6

    ruleNames =  [ "prog", "expr", "type", "type_neg", "decl", "assign_new", 
                   "assign" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    TYPE_NAME=13
    VAR=14
    INT=15
    FLOAT=16
    STRING=17
    BOOL=18
    COMMENT=19
    MULTICOMMENT=20
    NEWLINE=21
    WS=22

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.11.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(echoParser.EOF, 0)

        def decl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(echoParser.DeclContext)
            else:
                return self.getTypedRuleContext(echoParser.DeclContext,i)


        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(echoParser.ExprContext)
            else:
                return self.getTypedRuleContext(echoParser.ExprContext,i)


        def getRuleIndex(self):
            return echoParser.RULE_prog

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProg" ):
                return visitor.visitProg(self)
            else:
                return visitor.visitChildren(self)




    def prog(self):

        localctx = echoParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 20 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 16
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
                if la_ == 1:
                    self.state = 14
                    self.decl()
                    pass

                elif la_ == 2:
                    self.state = 15
                    self.expr(0)
                    pass


                self.state = 18
                self.match(echoParser.T__0)
                self.state = 22 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (((_la) & ~0x3f) == 0 and ((1 << _la) & 516672) != 0):
                    break

            self.state = 24
            self.match(echoParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return echoParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class VariableContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a echoParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def VAR(self):
            return self.getToken(echoParser.VAR, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariable" ):
                return visitor.visitVariable(self)
            else:
                return visitor.visitChildren(self)


    class ParentContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a echoParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(echoParser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParent" ):
                return visitor.visitParent(self)
            else:
                return visitor.visitChildren(self)


    class TypeExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a echoParser.ExprContext
            super().__init__(parser)
            self.value = None # TypeContext
            self.copyFrom(ctx)

        def type_(self):
            return self.getTypedRuleContext(echoParser.TypeContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypeExpr" ):
                return visitor.visitTypeExpr(self)
            else:
                return visitor.visitChildren(self)


    class OpExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a echoParser.ExprContext
            super().__init__(parser)
            self.left = None # ExprContext
            self.op = None # Token
            self.right = None # ExprContext
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(echoParser.ExprContext)
            else:
                return self.getTypedRuleContext(echoParser.ExprContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOpExpr" ):
                return visitor.visitOpExpr(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = echoParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 2
        self.enterRecursionRule(localctx, 2, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 33
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [14]:
                localctx = echoParser.VariableContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 27
                self.match(echoParser.VAR)
                pass
            elif token in [6, 15, 16, 17, 18]:
                localctx = echoParser.TypeExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 28
                localctx.value = self.type_()
                pass
            elif token in [9]:
                localctx = echoParser.ParentContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 29
                self.match(echoParser.T__8)
                self.state = 30
                self.expr(0)
                self.state = 31
                self.match(echoParser.T__9)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 46
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 44
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
                    if la_ == 1:
                        localctx = echoParser.OpExprContext(self, echoParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 35
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 36
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(((_la) & ~0x3f) == 0 and ((1 << _la) & 28) != 0):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 37
                        localctx.right = self.expr(6)
                        pass

                    elif la_ == 2:
                        localctx = echoParser.OpExprContext(self, echoParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 38
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 39
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==5 or _la==6):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 40
                        localctx.right = self.expr(5)
                        pass

                    elif la_ == 3:
                        localctx = echoParser.OpExprContext(self, echoParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 41
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 42
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==7 or _la==8):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 43
                        localctx.right = self.expr(3)
                        pass

             
                self.state = 48
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class TypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return echoParser.RULE_type

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class BoolTypeContext(TypeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a echoParser.TypeContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def BOOL(self):
            return self.getToken(echoParser.BOOL, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBoolType" ):
                return visitor.visitBoolType(self)
            else:
                return visitor.visitChildren(self)


    class StringTypeContext(TypeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a echoParser.TypeContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def STRING(self):
            return self.getToken(echoParser.STRING, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStringType" ):
                return visitor.visitStringType(self)
            else:
                return visitor.visitChildren(self)


    class TypeNegContext(TypeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a echoParser.TypeContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def type_neg(self):
            return self.getTypedRuleContext(echoParser.Type_negContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypeNeg" ):
                return visitor.visitTypeNeg(self)
            else:
                return visitor.visitChildren(self)


    class IntTypeContext(TypeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a echoParser.TypeContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INT(self):
            return self.getToken(echoParser.INT, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIntType" ):
                return visitor.visitIntType(self)
            else:
                return visitor.visitChildren(self)


    class FloatTypeContext(TypeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a echoParser.TypeContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def FLOAT(self):
            return self.getToken(echoParser.FLOAT, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFloatType" ):
                return visitor.visitFloatType(self)
            else:
                return visitor.visitChildren(self)



    def type_(self):

        localctx = echoParser.TypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_type)
        try:
            self.state = 54
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [15]:
                localctx = echoParser.IntTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 49
                self.match(echoParser.INT)
                pass
            elif token in [16]:
                localctx = echoParser.FloatTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 50
                self.match(echoParser.FLOAT)
                pass
            elif token in [17]:
                localctx = echoParser.StringTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 51
                self.match(echoParser.STRING)
                pass
            elif token in [18]:
                localctx = echoParser.BoolTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 52
                self.match(echoParser.BOOL)
                pass
            elif token in [6]:
                localctx = echoParser.TypeNegContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 53
                self.type_neg()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Type_negContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return echoParser.RULE_type_neg

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class FloatTypeNegContext(Type_negContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a echoParser.Type_negContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def FLOAT(self):
            return self.getToken(echoParser.FLOAT, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFloatTypeNeg" ):
                return visitor.visitFloatTypeNeg(self)
            else:
                return visitor.visitChildren(self)


    class IntTypeNegContext(Type_negContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a echoParser.Type_negContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INT(self):
            return self.getToken(echoParser.INT, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIntTypeNeg" ):
                return visitor.visitIntTypeNeg(self)
            else:
                return visitor.visitChildren(self)



    def type_neg(self):

        localctx = echoParser.Type_negContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_type_neg)
        try:
            self.state = 60
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                localctx = echoParser.IntTypeNegContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 56
                self.match(echoParser.T__5)
                self.state = 57
                self.match(echoParser.INT)
                pass

            elif la_ == 2:
                localctx = echoParser.FloatTypeNegContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 58
                self.match(echoParser.T__5)
                self.state = 59
                self.match(echoParser.FLOAT)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TYPE_NAME(self):
            return self.getToken(echoParser.TYPE_NAME, 0)

        def assign_new(self):
            return self.getTypedRuleContext(echoParser.Assign_newContext,0)


        def assign(self):
            return self.getTypedRuleContext(echoParser.AssignContext,0)


        def getRuleIndex(self):
            return echoParser.RULE_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecl" ):
                return visitor.visitDecl(self)
            else:
                return visitor.visitChildren(self)




    def decl(self):

        localctx = echoParser.DeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_decl)
        try:
            self.state = 66
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [13]:
                self.enterOuterAlt(localctx, 1)
                self.state = 62
                self.match(echoParser.TYPE_NAME)
                self.state = 63
                self.match(echoParser.T__10)
                self.state = 64
                self.assign_new()
                pass
            elif token in [14]:
                self.enterOuterAlt(localctx, 2)
                self.state = 65
                self.assign()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assign_newContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(echoParser.VAR, 0)

        def expr(self):
            return self.getTypedRuleContext(echoParser.ExprContext,0)


        def getRuleIndex(self):
            return echoParser.RULE_assign_new

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign_new" ):
                return visitor.visitAssign_new(self)
            else:
                return visitor.visitChildren(self)




    def assign_new(self):

        localctx = echoParser.Assign_newContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_assign_new)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 68
            self.match(echoParser.VAR)
            self.state = 69
            self.match(echoParser.T__11)
            self.state = 70
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(echoParser.VAR, 0)

        def expr(self):
            return self.getTypedRuleContext(echoParser.ExprContext,0)


        def getRuleIndex(self):
            return echoParser.RULE_assign

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign" ):
                return visitor.visitAssign(self)
            else:
                return visitor.visitChildren(self)




    def assign(self):

        localctx = echoParser.AssignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_assign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 72
            self.match(echoParser.VAR)
            self.state = 73
            self.match(echoParser.T__11)
            self.state = 74
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[1] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         




