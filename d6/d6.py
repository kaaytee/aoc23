import re

def sol(file):
    with open(file, 'r') as f:
        for fs in f:
            if "Time:" in fs:
                time = re.sub(r"Time:\s+", "", fs.rstrip())
                time = time.split()
            else:
                dist = re.sub(r"Distance:\s+", "", fs)
                dist = dist.split()

    ans = [] 
    print(time, dist)
    for i in range(0, len(time)):
        res = []
        for j in range(1, int(time[i]) + 1):
            if j == int(time[i]):
                continue
            ltime = int(time[i]) - j
            rdist = j * ltime
            print(ltime, rdist)
            if rdist > int(dist[i]):
                res.append(j)
        if len(res): 
            ans.append(len(res))
            
    res = 1
    for a in ans:
        res *= a
         
    return res



def sol2(file):
    with open(file, 'r') as f:
        for fs in f:
            if "Time:" in fs:
                time = re.sub(r"Time:\s+", "", fs.rstrip())
                time = int(re.sub(r"\s+", "", time))

            else:
                dist = re.sub(r"Distance:\s+", "", fs)
                dist = int(re.sub(r"\s+", "", dist))

        res = [] 
        for i in range(1, time + 1):
            if i == int(time):
                continue
            ltime = int(time) - i
            rdist = i * ltime
            if rdist > int(dist):
                res.append(i)
                
    return len(res)

        
if __name__ == "__main__":
    print(sol2('input1.txt'))