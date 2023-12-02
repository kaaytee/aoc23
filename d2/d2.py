import re

maxR = 12 
maxG = 13
maxB = 14

def sol(file):
    lnum = []
    with open(file, 'r') as f:
        count = 1
        for lines in f:
            guy = False
            boxes = []
            lines = re.sub(r'^Game\s[0-9].*:', '', lines)
            lines = re.sub(r'\s+', '', lines)
            boxes = lines.split(';')
            for b in boxes:
                bboxes = []
                bboxes = b.split(',')
                for bb in bboxes:
                    if 'red' in bb:
                        bb = re.sub(r'[A-Za-z]', '', bb)       
                        if int(bb) > maxR:
                            guy = True
                            break
                    elif 'green' in bb:
                        bb = re.sub(r'[A-Za-z]', '', bb)       
                        if int(bb) > maxG:
                            guy = True
                            break
                    elif 'blue' in bb:
                        bb = re.sub(r'[A-Za-z]', '', bb)       
                        if int(bb) > maxB:
                            guy = True
                            break
            
                if guy:
                    break
            if not guy:
                lnum.append(count)                
            count += 1
    return sum(lnum)

def sol2(file):
    nums = []
    with open(file, 'r') as f:
        for lines in f:
            r = 0
            g = 0
            bs = 0
            boxes = []
            lines = re.sub(r'^Game\s[0-9].*:', '', lines)
            lines = re.sub(r'\s+', '', lines)
            boxes = lines.split(';')
            for b in boxes:
                bboxes = []
                bboxes = b.split(',')
                for bb in bboxes:
                    if 'red' in bb:
                        bb = re.sub(r'[A-Za-z]', '', bb)       
                        if r < int(bb):
                            r = int(bb)
                    elif 'green' in bb:
                        bb = re.sub(r'[A-Za-z]', '', bb)       
                        if g < int(bb):
                            g = int(bb)
                    elif 'blue' in bb:
                        bb = re.sub(r'[A-Za-z]', '', bb)
                        if bs < int(bb):
                            bs = int(bb)
                
            nums.append(r * g * bs)
    return sum(nums)

if __name__ == "__main__":
    print(sol("input.txt"), sol2('input.txt'))