grammar echo;

prog: ((decl | expr) ';')+ EOF;

expr: VAR # Variable
    | left=expr op=('*' | '/' | '**') right=expr # OpExpr
    | left=expr op=('+' | '-') right=expr # OpExpr
    | value=type # TypeExpr
    | '(' expr ')' # Parent
    ;

TYPE_NAME: ('int' | 'float' | 'string');
type: INT # IntType
| FLOAT # FloatType
| STRING # StringType
| type_neg # TypeNeg
;
type_neg: '-' INT # IntTypeNeg
| '-' FLOAT # FloatTypeNeg
;

decl: TYPE_NAME ':' assign | assign;
assign: VAR '=' expr;

VAR: [a-zA-Z_][a-zA-Z0-9_]*;

INT: [0-9]+;
FLOAT: [0-9]+ '.' [0-9]+;
STRING: '"' .*? '"' | '\'' .*? '\'';


COMMENT: '//' ~[\r\n]* -> skip;
MULTICOMMENT: '/*' .*? '*/' -> skip;
NEWLINE: [\r\n\f]+ -> skip;
WS: [ \t]+ -> skip;
