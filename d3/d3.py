


def get_graph(file):
    g = []
    with open(file, 'r') as f:
        for l in f:
            l = l.strip()
            g.append(list(l))
        
        
    return g
        
def sol(g):
    cds = set()
    
    for r, row in enumerate(g):
        for c, col in enumerate(row):
            if not col.isdigit() and col != '.':
                for rs in [r - 1, r, r + 1]:
                    for cs in [c - 1, c, c + 1]:
                        if rs < 0 or rs >= len(g) or cs < 0 or cs >= len(g[rs]):
                            continue 
                        if g[rs][cs].isdigit():
                            while cs > 0 and g[rs][cs - 1].isdigit():
                                cs -= 1
                            cds.add((rs, cs)) 

    ns = []
    for r, c in cds:
        s = ""
        while c < len(g[r]) and g[r][c].isdigit():
            s += g[r][c]
            c += 1
        ns.append(int(s))
        
    return sum(ns)
                
def sol2(g):
    cds = set()
    for r, row in enumerate(g):
        for c, col in enumerate(row):
            if col == '*':
                ccds = []
                for rs in [r - 1, r, r + 1]:
                    for cs in [c - 1, c, c + 1]:
                        if rs < 0 or rs >= len(g) or cs < 0 or cs >= len(g[rs]):
                            continue 
                        if g[rs][cs].isdigit():
                            while cs > 0 and g[rs][cs - 1].isdigit():
                                cs -= 1
                            if not (rs, cs) in ccds:
                                ccds.append((rs, cs)) 
                if len(ccds) == 2:
                    cds.add((ccds[0], ccds[1]))

    xs = []
    for x,y  in cds:
        r, c = x
        rs, cs = y    
        s = ""
        while c < len(g[r]) and g[r][c].isdigit():
            s += g[r][c]
            c += 1
        x = int(s)    
        s = ""
        while cs < len(g[rs]) and g[rs][cs].isdigit():
            s += g[rs][cs]
            cs += 1
        y = int(s)
        xs.append(x * y)               
        

    return sum(xs)

        
if __name__ =="__main__": 
    g = get_graph('input.txt')
    print(sol(g), sol2(g))

