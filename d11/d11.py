grid = []
with open('sample.txt', 'r') as f:
    for l in f:
        grid.append(list(l.strip()))


empty_rows = [r for r, row in enumerate(grid) if all(ch == '.' for ch in row)]
empty_col = [c for c, col in enumerate(zip(*grid)) if all(ch == '.' for ch in col)]

print(empty_rows, empty_col)
