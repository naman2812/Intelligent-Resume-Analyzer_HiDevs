n = int(input().strip())
best_candidate = None
max_exp = -1

for _ in range(n):
    line = input().strip().split()
    if len(line) >= 2:
        name = line[0]
        exp = int(line[1])
        
        if exp > max_exp:
            max_exp = exp
            best_candidate = name

if best_candidate is not None:
    print(f"Best candidate: {best_candidate}")
    print(f"Experience: {max_exp} years")
