import re

def sol(file):

    with open(file, 'r') as f:
        path = list(f.readline().strip())
        nodes = f.readlines()[1:]
        nodes = list(map(lambda s: s.strip(), nodes))
        
    d = {}
    for node in nodes:
        node = re.sub(r"=", '', node)
        n, instructions = node.split('  ')
        d[n] = tuple(instructions.strip('()').split(', '))
    
    count = 0
    pos = "AAA"
    i = 0
    while i < len(path):
        if pos == 'ZZZ':
            break
        values = d[pos]
        if path[i] == "L":
            pos = values[0]
        else:
            pos = values[1]
        count += 1
        i += 1
        if i == len(path) and pos != 'ZZZ':
            i = 0
        
        
    print(count)

def sol2(file):
    with open(file, 'r') as f:
        path = list(f.readline().strip())
        nodes = f.readlines()[1:]
        nodes = list(map(lambda s: s.strip(), nodes))
        
    d = {}
    starts = [] 
    for node in nodes:
        node = re.sub(r"=", '', node)
        n, instructions = node.split('  ')
        if 'A' in n:
            starts.append(n)
        d[n] = tuple(instructions.strip('()').split(', '))

    print(d)
    print(starts)


sol2('input.txt')