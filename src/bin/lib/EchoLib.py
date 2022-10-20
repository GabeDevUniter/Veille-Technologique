
variables = {}

def GetVariable(var):
    return variables[var][1]

def DeclareVariable(var, type, value):
    value = ConvertValue(type, value)
    variables[var] = [type, value]

types = {
'int':int,
'float':float,
'string':str
}

def ConvertValue(type, value):
    return types[type](value)
