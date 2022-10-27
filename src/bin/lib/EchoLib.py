
variables = {}

def GetVariable(var):
    try:
        return variables[var][1]
    except KeyError:
        return 'Variable not defined.'

def DeclareVariable(type, var, value):
    value = ConvertValue(type, value)
    variables[var] = [type, value]

def AssignVariable(var, value):
    try:
        value = ConvertValue(variables[var][0], value)
        variables[var][1] = value
    except KeyError:
        print('Variable not defined.')


types = {
'int':int,
'float':float,
'string':str,
'str':str,
'bool':bool,
}

def ConvertValue(type, value):
    return types[type](value)
