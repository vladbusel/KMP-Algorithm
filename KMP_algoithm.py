import time
import numpy as np

def prefix_function(S):
    p = [0]
    for i in range(1,len(S)):
        k = p[i-1]
        while  k > 0 and S[i] != S[k]:
            k = p[k-1]
        if S[i] == S[k]:
            k += 1
        p.append(k)
    return p

def kmp(S,T):
    j = 0
    A = []
    pf = prefix_function(S)
    for i in range(len(T)):
        while j > 0 and T[i] != S[j]:
            j = pf[j-1]
        if T[i] == S[j]:
            j += 1
        if j == len(S):
            A.append(i-len(S)+1)
            j = pf[j-1]
    return A

def main():
    file = open("test.txt")
    test = file.read().split('\n')[:-1]
    part_S = test[0].split(' ')
    part_T = [t.split(' ') for t in test[1:]]
    parts = {part_S[i]: part_T[i] for i in range(len(part_S))}
    file.close()
    A = []
    Timer = []
    for S in parts.keys():
        a = []
        for T in parts.get(S):
            start_time = time.time()
            a.append(kmp(S,T))
            Timer.append(time.time() - start_time)
        A.append(a)
    #print(A)
    print(np.mean(np.array(Timer)))

if __name__ == "__main__":
    main()
