grid = []
with open('sample.txt', 'r') as f:
    for lines in f:
        grid.append(list(lines.strip()))
        
# up left down right
direction = ['U', 'L', 'D', 'R']
cycles = 0
dir_count = 0
grids = []
while cycles < 1000000000:
    ddir = direction[dir_count]
    if grid in grids:
        continue
    for r, row in enumerate(grid):
        for c, col in enumerate(grid[r]):
            if col == 'O' :
                if ddir == 'U':
                    c_r = r
                    while c_r > 0:
                        if grid[c_r - 1][c] == '#':
                            break
                        if grid[c_r - 1][c] == '.':
                            grid[c_r][c] = '.'
                            grid[c_r - 1][c] = 'O'
                        c_r -= 1
                elif ddir == 'L':
                    c_c = c
                    while c_c > 0:
                        if grid[r][c_c - 1] == '#':
                            break
                        if grid[r][c_c - 1] == '.':
                            grid[r][c_c] = '.'
                            grid[r][c_c -1] = 'O'
                        c_c -= 1
                    
                elif ddir == 'D':
                    c_r = r
                    while c_r < len(grid) - 1:
                        if grid[c_r + 1][c] == '#':
                            break
                        if grid[c_r + 1][c] == '.':
                            grid[c_r][c] = '.'
                            grid[c_r + 1][c] = 'O'
                        c_r += 1
                else: 
                    c_c = c
                    while c_c > len(grid[r]) - 1:
                        if grid[r][c_c + 1] == '#':
                            break
                        if grid[r][c_c + 1] == '.':
                            grid[r][c_c] = '.'
                            grid[r][c_c + 1] = 'O'
                        c_c += 1
    if dir_count == 3:
        dir_count = 0
        cycles += 1
        if grid not in grids:
            grids.append(grid)
    else:
        dir_count += 1 
    
total = 0            
for r, row in enumerate(grid):
    count = 0
    for c, col in enumerate(grid[r]):
        if col == 'O':
            count += 1
    
    total += (len(grid) - r) * count

print(total)