grammar echo;

prog: ((decl ';' | expr ';' | block))+ EOF;


/**-------EXPRESSION-------**/
expr: func # FuncCall
    | VAR # Variable
    | left=expr op=('*' | '/' | '**') right=expr # OpExpr
    | left=expr op=('+' | '-') right=expr # OpExpr
    | value=type # TypeExpr
    | left=expr op=('<<' | '>>') right=expr # OpExpr
    | left=expr op=('==' | '<' | '<=' | '>' | '>=' | '!=') right=expr # CompExpr
    | left=expr op=('&&' | '||') right=expr # CompLogic
    | '(' expr ')' # Parent
    ;


/**-------BLOCKS-------**/
block: 'if' expr # IfBlock
     | 'elif' expr # ElifBlock
     | 'else' # ElseBlock
     | 'endif' # EndIfBlock

     | 'for' iter=assign_new 'to' max=expr # ForBlock
     | 'for' iter=assign_new 'to' max=expr 'next' next=expr # ForNextBlock
     | 'endfor' # EndForBlock
     | 'function' func # FunctionBlock
     | 'endfunction' # EndFunctionBlock
     ;


/**-------DATA TYPES-------**/
TYPE_NAME: ('int' | 'float' | 'string' | 'str' | 'bool');
type: type_num # NumType
| STRING # StringType
| BOOL # BoolType
;
type_num: INT # IntType
| FLOAT # FloatType
| type_neg # TypeNeg
;
type_neg: '-' INT # IntTypeNeg
| '-' FLOAT # FloatTypeNeg
;

/**-------ASSIGNMENTS-------**/
decl: TYPE_NAME ':' assign_new | assign;
assign_new: VAR '=' expr;
assign: VAR assign_op expr # AssignRegular
      | VAR '++' # AssignInc
      | VAR '--' # AssignDec
;
assign_op: '=' | '+=' | '-=' | '*=' | '/=' | '**=';


/**-------FUNCTION CALL-------**/
func: VAR '(' (expr (',' expr)*)* ')';


/**-------VARIABLES-------**/
VAR: [a-zA-Z_][a-zA-Z0-9_]*;

INT: [0-9]+;
FLOAT: [0-9]+ '.' [0-9]+;
STRING: '"' .*? '"' | '\'' .*? '\'';
BOOL: 'true' | 'false';


/**-------COMMENTS AND BLANKS-------**/
COMMENT: '//' ~[\r\n]* -> skip;
MULTICOMMENT: '/*' .*? '*/' -> skip;
NEWLINE: [\r\n\f]+ -> skip;
WS: [ \t]+ -> skip;
