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
        4,1,19,67,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,1,0,1,
        0,3,0,15,8,0,1,0,1,0,4,0,19,8,0,11,0,12,0,20,1,0,1,0,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,3,1,32,8,1,1,1,1,1,1,1,1,1,1,1,1,1,5,1,40,8,1,10,
        1,12,1,43,9,1,1,2,1,2,1,2,1,2,3,2,49,8,2,1,3,1,3,1,3,1,3,3,3,55,
        8,3,1,4,1,4,1,4,1,4,3,4,61,8,4,1,5,1,5,1,5,1,5,1,5,0,1,2,6,0,2,4,
        6,8,10,0,2,1,0,2,4,1,0,5,6,71,0,18,1,0,0,0,2,31,1,0,0,0,4,48,1,0,
        0,0,6,54,1,0,0,0,8,60,1,0,0,0,10,62,1,0,0,0,12,15,3,8,4,0,13,15,
        3,2,1,0,14,12,1,0,0,0,14,13,1,0,0,0,15,16,1,0,0,0,16,17,5,1,0,0,
        17,19,1,0,0,0,18,14,1,0,0,0,19,20,1,0,0,0,20,18,1,0,0,0,20,21,1,
        0,0,0,21,22,1,0,0,0,22,23,5,0,0,1,23,1,1,0,0,0,24,25,6,1,-1,0,25,
        32,5,12,0,0,26,32,3,4,2,0,27,28,5,7,0,0,28,29,3,2,1,0,29,30,5,8,
        0,0,30,32,1,0,0,0,31,24,1,0,0,0,31,26,1,0,0,0,31,27,1,0,0,0,32,41,
        1,0,0,0,33,34,10,4,0,0,34,35,7,0,0,0,35,40,3,2,1,5,36,37,10,3,0,
        0,37,38,7,1,0,0,38,40,3,2,1,4,39,33,1,0,0,0,39,36,1,0,0,0,40,43,
        1,0,0,0,41,39,1,0,0,0,41,42,1,0,0,0,42,3,1,0,0,0,43,41,1,0,0,0,44,
        49,5,13,0,0,45,49,5,14,0,0,46,49,5,15,0,0,47,49,3,6,3,0,48,44,1,
        0,0,0,48,45,1,0,0,0,48,46,1,0,0,0,48,47,1,0,0,0,49,5,1,0,0,0,50,
        51,5,6,0,0,51,55,5,13,0,0,52,53,5,6,0,0,53,55,5,14,0,0,54,50,1,0,
        0,0,54,52,1,0,0,0,55,7,1,0,0,0,56,57,5,11,0,0,57,58,5,9,0,0,58,61,
        3,10,5,0,59,61,3,10,5,0,60,56,1,0,0,0,60,59,1,0,0,0,61,9,1,0,0,0,
        62,63,5,12,0,0,63,64,5,10,0,0,64,65,3,2,1,0,65,11,1,0,0,0,8,14,20,
        31,39,41,48,54,60
    ]

class echoParser ( Parser ):

    grammarFileName = "echo.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "';'", "'*'", "'/'", "'**'", "'+'", "'-'", 
                     "'('", "')'", "':'", "'='" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "TYPE_NAME", 
                      "VAR", "INT", "FLOAT", "STRING", "COMMENT", "MULTICOMMENT", 
                      "NEWLINE", "WS" ]

    RULE_prog = 0
    RULE_expr = 1
    RULE_type = 2
    RULE_type_neg = 3
    RULE_decl = 4
    RULE_assign = 5

    ruleNames =  [ "prog", "expr", "type", "type_neg", "decl", "assign" ]

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
    TYPE_NAME=11
    VAR=12
    INT=13
    FLOAT=14
    STRING=15
    COMMENT=16
    MULTICOMMENT=17
    NEWLINE=18
    WS=19

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
            self.state = 18 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 14
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
                if la_ == 1:
                    self.state = 12
                    self.decl()
                    pass

                elif la_ == 2:
                    self.state = 13
                    self.expr(0)
                    pass


                self.state = 16
                self.match(echoParser.T__0)
                self.state = 20 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (((_la) & ~0x3f) == 0 and ((1 << _la) & 63680) != 0):
                    break

            self.state = 22
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
            self.state = 31
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [12]:
                localctx = echoParser.VariableContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 25
                self.match(echoParser.VAR)
                pass
            elif token in [6, 13, 14, 15]:
                localctx = echoParser.TypeExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 26
                localctx.value = self.type_()
                pass
            elif token in [7]:
                localctx = echoParser.ParentContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 27
                self.match(echoParser.T__6)
                self.state = 28
                self.expr(0)
                self.state = 29
                self.match(echoParser.T__7)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 41
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 39
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
                    if la_ == 1:
                        localctx = echoParser.OpExprContext(self, echoParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 33
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 34
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(((_la) & ~0x3f) == 0 and ((1 << _la) & 28) != 0):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 35
                        localctx.right = self.expr(5)
                        pass

                    elif la_ == 2:
                        localctx = echoParser.OpExprContext(self, echoParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 36
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 37
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==5 or _la==6):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 38
                        localctx.right = self.expr(4)
                        pass

             
                self.state = 43
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
            self.state = 48
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [13]:
                localctx = echoParser.IntTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 44
                self.match(echoParser.INT)
                pass
            elif token in [14]:
                localctx = echoParser.FloatTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 45
                self.match(echoParser.FLOAT)
                pass
            elif token in [15]:
                localctx = echoParser.StringTypeContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 46
                self.match(echoParser.STRING)
                pass
            elif token in [6]:
                localctx = echoParser.TypeNegContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 47
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
            self.state = 54
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                localctx = echoParser.IntTypeNegContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 50
                self.match(echoParser.T__5)
                self.state = 51
                self.match(echoParser.INT)
                pass

            elif la_ == 2:
                localctx = echoParser.FloatTypeNegContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 52
                self.match(echoParser.T__5)
                self.state = 53
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
            self.state = 60
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [11]:
                self.enterOuterAlt(localctx, 1)
                self.state = 56
                self.match(echoParser.TYPE_NAME)
                self.state = 57
                self.match(echoParser.T__8)
                self.state = 58
                self.assign()
                pass
            elif token in [12]:
                self.enterOuterAlt(localctx, 2)
                self.state = 59
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
        self.enterRule(localctx, 10, self.RULE_assign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 62
            self.match(echoParser.VAR)
            self.state = 63
            self.match(echoParser.T__9)
            self.state = 64
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
                return self.precpred(self._ctx, 4)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 3)
         




