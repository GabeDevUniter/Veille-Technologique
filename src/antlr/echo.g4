grammar echo;

prog: ((decl | expr) ';')+ EOF;

expr: VAR # Variable
    | left=expr op=('*' | '/' | '**') right=expr # OpExpr
    | left=expr op=('+' | '-') right=expr # OpExpr
    | TYPE # VariableType
    | '(' expr ')' # Parent
    ;

TYPE_NAME: 'int' | 'float' | 'string';
TYPE: INT | FLOAT | STRING;

decl: TYPE_NAME ':' assign | assign;
assign: VAR '=' expr;

VAR: [a-zA-Z][a-zA-Z0-9]*;

INT: [0-9]+;
FLOAT: [0-9]+ '.' [0-9]+;
STRING: '"' .*? '"' | '\'' .*? '\'';


COMMENT: '//' ~[\r\n]* -> skip;
NEWLINE: [\r\n\f]+ -> skip;
WS: [ \t]+ -> skip;
