grammar echo;

prog: ((decl | expr) ';')+ EOF;

expr: VAR # Variable
    | left=expr op=('*' | '/' | '**') right=expr # OpExpr
    | left=expr op=('+' | '-') right=expr # OpExpr
    | value=type # TypeExpr
    | left=expr op=('<<' | '>>') right=expr # OpExpr
    | '(' expr ')' # Parent
    ;

TYPE_NAME: ('int' | 'float' | 'string' | 'str' | 'bool');
type: INT # IntType
| FLOAT # FloatType
| STRING # StringType
| BOOL # BoolType
| type_neg # TypeNeg
;
type_neg: '-' INT # IntTypeNeg
| '-' FLOAT # FloatTypeNeg
;

decl: TYPE_NAME ':' assign_new | assign;
assign_new: VAR '=' expr;
assign: VAR '=' expr;

VAR: [a-zA-Z_][a-zA-Z0-9_]*;

INT: [0-9]+;
FLOAT: [0-9]+ '.' [0-9]+;
STRING: '"' .*? '"' | '\'' .*? '\'';
BOOL: 'true' | 'false';


COMMENT: '//' ~[\r\n]* -> skip;
MULTICOMMENT: '/*' .*? '*/' -> skip;
NEWLINE: [\r\n\f]+ -> skip;
WS: [ \t]+ -> skip;
