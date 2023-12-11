import re

def sol(file):
    with open (file, 'r') as f:
        tsum = 0
        count = 1
        for l in f:
            l = re.sub(r'Card\s[0-9]+\:\s', '', l).rstrip()
            l = l.split('|')
            ws = l[0].split(' ')
            cs = l[1].split(' ')

            
            ms = []
            for w in ws:
                for c in cs:
                    if c == w and c != ' ' and c != '':
                        ms.append(c)
                        break
            if len(ms):
                tsum += 2**(len(ms)-1)        
    return tsum
    
def sol2(file):
    with open (file, 'r') as f:
        card = 1
        d = {}
        for l in f:
            l = re.sub(r'Card\s[0-9]+\:\s', '', l).rstrip()
            l = l.split('|')
            ws = l[0].split(' ')
            cs = l[1].split(' ')

            
            ms = []
            for w in ws:
                for c in cs:
                    if c == w and c != ' ' and c != '':
                        ms.append(c)
                        break
            if len(ms):
                if card not in d:
                    d[card] = 1
                else:
                    d[card] += 1
                for i in range(1, (len(ms) + 1)):
                    if card + i not in d:
                        d[card + i] = d[card]
                    else:
                        d[card + i] += d[card]
            else:
                if card not in d:
                    d[card] = 1
                else:
                    d[card] += 1

            card += 1
        ssum = 0
        for i, j in enumerate(d):
            ssum += d[j]
        return ssum
        

# 1 -> 1
# 2 -> 1 + 2
# 3 -> 1 + 2 + 2 + 3
# 4 -> 1 + 2 + 2 + 3 + 3 + 3 + 3 + 4
# 5 -> 1 + 3 + 3 + 3 + 3 + 4 + 4 + 4 + 4 + 4 + 4 + 4 + 4
# 6 -> 
    
    

if __name__ == "__main__":
    print(sol2("input2.txt"))
    