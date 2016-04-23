namespaces = {'global': {'parent': None, 'var':[]}}

n = int(input())
# n = 11

def get_namespase(namespace, var):
    enviroment = namespaces[namespace]
    '''
    print('namespace', namespace, type(namespace))
    print('var', var, type(var))
    print('enviroment', enviroment, type(enviroment))
    print('enviroment[parent]', enviroment['parent'], type(enviroment['parent']))
    print("var == enviroment['var']", var == enviroment['var'])
    '''
    if var in enviroment['var']:
        return namespace
    elif enviroment['parent'] is None:
        return None
    else:
        return get_namespase(enviroment['parent'], var)

for command in range(n):
    query, namespace, var = input().split()

    if query == 'create':
        namespaces[namespace] = {'parent':var,'var':[]}
    elif query == 'add':
        namespaces[namespace]['var'].append(var)
    elif query == 'get':
        ans = get_namespase(namespace, var)
        print(ans)
