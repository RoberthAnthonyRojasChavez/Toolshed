def combos(O,n):
    if (n <= 0): return
    for s in O:
        if len(s) <= n: yield s
        for t in combos(O,n-len(s)): yield s+t
for x in combos(["A","T","G","C"],10): #format as: combos(O,n); where 0 = bases options and n = max length of sequence
    with open(r"C:\Users\rojaschavez\Desktop\Check\Trial.txt", 'a') as f:   #change output directory here
        f.write(x)
        f.write('\n')
