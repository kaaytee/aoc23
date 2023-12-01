import re 

def sol(file):
    total = 0
    with open(file, 'r') as f:
        for lines in f:
            lines = re.sub(r'[a-zA-Z]', '', lines).rstrip()
            llen = len(lines)
            if llen == 1:
                total += int(lines[0]*2)
            else:                
                total += int(lines[0] + lines[-1])
    return total

def sol2(file):
    l =  {'one': 1 , 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}

    total = 0
    count = 1
    with open(file, 'r') as f:
        for lines in f:
            print(str(count) + ' ', end='')
            for i in l:
                lines = re.sub(rf"{i}", i + str(l[i]) + i, lines).rstrip()
            lines = re.sub(r'[a-zA-Z]', '', lines).rstrip()            
            llen = len(lines)
            if llen == 1:
                total += int(lines[0]*2)
            else:                
                total += int(lines[0] + lines[-1])
            count += 1
    return total

if __name__ == "__main__":
    print(sol('input.txt'), sol2('input.txt'))
