import random
import string

def words_generator(length, number=1, S='', repetitions=1):
    pool = string.ascii_letters
    seen = set()
    if length >= len(S):
        while len(seen) < number:
            word = ''
            for i in range(repetitions):
                k=random.randint(-len(S),length-len(word)-repetitions*len(S))
                if k < 0:
                    word = word[:-k]+S
                else:
                    word += ''.join(random.choices(pool, k = k))+S
            word += ''.join(random.choices(pool, k = length-len(word)))
            seen.add(word)
    return seen

def main():
    file = open('test.txt','w')
    m = 800
    n = 40000
    repetitions = int(((n/m)*3)//10)
    set_S = words_generator(m,100)
    set_T = []
    for S in set_S:
        set_T.append(words_generator(n,1,S,repetitions))
    str_T = ''
    for word in set_T:
        str_T += ' '.join(word) + '\n'
    str_S = ' '.join(word for word in set_S) + '\n'
    file.write(str_S+str_T)
    file.close()

if __name__ == "__main__":
    main()
