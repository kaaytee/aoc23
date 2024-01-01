
seeds, *blocks = open('inp.txt').read().split("\n\n")

seeds = list(map(int,seeds.split(":")[1].split()))
        
for block in blocks:
    new_seeds = []
    for nums in block.split('\n')[1:]:
        dest_range, src_range, range_len = list(map(int, nums.split())) 
        print(dest_range, src_range, range_len)
        
    
    print()