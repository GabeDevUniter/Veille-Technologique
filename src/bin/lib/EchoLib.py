
variables = {}

types = {
'int':int,
'float':float,
'string':str,
'str':str,
'bool':bool,
}

def ConvertValue(type, value):
    return types[type](value)

functions = {}

functionTemplate = {
0: [], # Block instructions
'label': None,
'params': None,
'returnType': None,
'returnValue': None
}

functionReturnTypes = {'void':'void'}
functionReturnTypes.update(types)

def AddFunction(scope):
    functions[scope['label']] = scope.copy()

def AddFunctionFromTemplate(label, params=None, returnType='void'):
    newFunction = functionTemplate.copy()

    newFunction['label'] = label
    newFunction['params'] = params
    newFunction['returnType'] = returnType

    functions[label] = newFunction

def CallFunction(label):
    pass

# index 0 in scopes is a list of instructions to execute within the scope
# (useful for IF and FOR scopes)
scopes = {
    'global': {
        # 'if': {
        #   0:['a += 5;', 'b = a;'],
        #   1: ctx, # For an if statement, store the condition
        #   2: scopeIndex,
        #
        #   'a':('str', 'fsfau'),
        #
        #   'b':('float',10.5),
        # }
        # 'for': {
        #   0:['a += 5;', 'b = a;'],
        #   1: 5, # For a for statement, store the iteration value
        #   2: 10, # For a for statement, store the max value
        #   3: 1, # For a for statement, store the step value
        #   4: scopeIndex,
        #
        #   'i':('int', '0'),
        # }
        #
        # 'a':('str', 'fsfau'),
        #
        # 'b':('float',10.5),
    }
}

currentScope = ['global']

def FindVariable(var):
    vars = []
    scope = scopes
    for key in currentScope:
        scope = scope[key]
        if var in scope:
            vars.append(scope[var])

    return vars[-1] if len(vars) > 0 else None

# Merci à mgilson pour sa fonction https://stackoverflow.com/a/15210253
def GetScopes(d, value):
    for k,v in d.items():
        if isinstance(v, dict):
            p = find_key(v, value)
            if p:
                return [k] + p
        elif v == value:
            return [k]

def GetCurrentScope():
    scope = scopes
    for key in currentScope:
        scope = scope[key]
    return scope

def GetScopeAt(n):
    scope = scopes
    maxIndex = n if n >= 0 else len(currentScope) + n
    scopeIndex = -1
    for key in currentScope:
        scopeIndex += 1

        if scopeIndex == maxIndex:
            return scope[key]

        scope = scope[key]

def AddScope(label):
    scope = scopes
    scopeIndex = -1
    for key in currentScope:
        scopeIndex += 1

        if scopeIndex == len(currentScope) - 1:
            scope[key][label] = {0:[]}
            break

        scope = scope[key]

    currentScope.append(label)

def PopScope():
    if currentScope[-1] != 'global':
        scope = scopes
        scopeIndex = -1
        for key in currentScope:
            scopeIndex += 1

            if scopeIndex == len(currentScope) - 1:
                del scope[key]
                break

            scope = scope[key]

        #currentScope.remove(currentScope[-1])
        currentScope.pop()
        print(currentScope)


def GetVariable(var):
    try:
        #return variables[var][1]
        return FindVariable(var)[1]
    except (KeyError, TypeError):
        raise Exception('Variable %s is not defined.' % var)

def IsDefined(var):
    return FindVariable(var) != None

def DeclareVariable(type, var, value):
    value = ConvertValue(type, value)
    GetCurrentScope()[var] = [type, value]
    #print(GetCurrentScope())
    #variables[var] = [type, value]

def AssignVariable(var, value):
    try:
        # value = ConvertValue(variables[var][0], value)
        # variables[var][1] = value
        var = FindVariable(var)
        #print(var)
        value = ConvertValue(var[0], value)
        var[1] = value
    except (KeyError, TypeError):
        raise Exception('Variable %s is not defined.' % var)
