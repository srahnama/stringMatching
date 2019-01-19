from timeit import default_timer as timer

def NaiveSearch(pat, txt): 
    lst=[]
    start = timer()
    M = len(pat) 
    N = len(txt) 
    i = 0
  
    while i <= N-M: 
        for j in range(M): 
            if txt[i+j] != pat[j]: 
                break
            j += 1
  
        if j == M:     
            lst.append(i)
            i = i + M 
        
        elif j == 0: 
            i = i + 1
        else: 
            i = i + j     
    end = timer()
    tm=end-start
    t="%.8f"%tm
    return t,lst        


def RabinSearch(pat, txt): 
    start1 = timer()
    lst=[]
    q = 101  
    d = 256
    M = len(pat) 
    N = len(txt) 
    i = 0
    j = 0
    p = 0    
    t = 0     
    h = 1
  
    # The value of h would be "pow(d, M-1)%q" 
    for i in range(M-1): 
        h = (h*d)%q 
  
    for i in range(M): 
        p = (d*p + ord(pat[i]))%q 
        t = (d*t + ord(txt[i]))%q 
  
 
    for i in range(N-M+1): 
        if p == t: 
            for j in range(M): 
                if txt[i+j] != pat[j]: 
                    break
  
            j+=1
            if j==M: 
                lst.append(i) 
        if i < N-M: 
            t = (d*(t-ord(txt[i])*h) + ord(txt[i+M]))%q 
  
            #delete or not? 
            if t < 0: 
                t = t+q 
    end1=timer()
    tim=end1-start1
    ntm="%.8f"%tim
    return ntm,lst
            

def KMPSearch(pat, txt): 
    start=timer()
    lst=[]
    M = len(pat) 
    N = len(txt) 
  
    #lps : longest prefix suffix  
    lps = [0]*M 
    j = 0 
   
    computeLPSArray(pat, M, lps) 
  
    i = 0
    while i < N: 
        if pat[j] == txt[i]: 
            i += 1
            j += 1
  
        if j == M: 
            # print("Found pattern at index "+str(i-j))
            lst.append(str(i-j))
            j = lps[j-1] 
  
        # mismatch after j matches 
        elif i < N and pat[j] != txt[i]: 
            if j != 0: 
                j = lps[j-1] 
            else: 
                i += 1
    end=timer()
    tme=end-start
    rtme="%.8f"%tme
    return rtme,lst
     
def computeLPSArray(pat, M, lps): 
    len = 0 # length of the previous longest prefix suffix 
    lps[0] # lps[0] is always 0 
    i = 1
  
    # the loop calculates lps[i] for i = 1 to M-1 
    while i < M: 
        if pat[i]== pat[len]: 
            len += 1
            lps[i] = len
            i += 1
        else: 
            if len != 0: 
                len = lps[len-1] 
            else: 
                lps[i] = 0
                i += 1

import string
def FiniteAutomatonMatcher(pattern, line):
    patternLength = ((int)(len(pattern)))
    lst=[]
    start = timer()
    li = []
    for i in range(0,256):
        code = chr(i)
        li.append(code)
    li = ','.join(li)
    
    alphabet = li.replace(',','')+','#string.printable #ascii
    # print(string.printable)
    # text = 'shahab rahnama'
    StateMachine = ComputeTransitionFunction(pattern, alphabet)
    n = len(line)
    stateNumber = 0
    count = 0

    for i in range(n):
        stateNumber = StateMachine[stateNumber][line[i]]
        if stateNumber == patternLength:
            count += 1
            # print(i-(patternLength-1)
            lst.append(i - patternLength + 1)
    end = timer()
    tme = end-start
    rtme = "%.8f"%tme
    return rtme, lst


def ComputeTransitionFunction(pattern, alphabet):
    m = len(pattern)
    StateMachine = {}

    for i in range(m + 1):
        StateMachine[i] = {}
        for letter in alphabet:
            k = min(m, i + 1)
            while not (pattern[:i] + letter).endswith(pattern[:k]):
                # print(pattern[:i] + letter , pattern[:k])
                k -= 1
            StateMachine[i][letter] = k
    # print(StateMachine)
    return StateMachine




def main():
    
    
    with open('Patterns.txt', 'r') as myfile:
        patterns=myfile.read()
    patterns = patterns.split('\r\n')
    del patterns[((int)(len(patterns))-1)]

    with open('aesop11.txt', 'r') as myfile:
        data=myfile.read().replace('\n', '')
    # print(patterns)
    file = open('aesop11_result.json','w')
 
    file.write('{   ')
    
    for i in range(0,((int)(len(patterns))-1)):
        # file.write(patterns[i])
    
        tm,lst = NaiveSearch(patterns[i],data)
        file.write('NaiveSearch')        
        file.write(str(i))
        file.write(':')
        mydic = {'type':'NaiveSearch','time':tm,'list':lst,'file':'aesop11', 'pattern':patterns[i]}
        file.write(str(mydic))
        file.write(',')

        tm,lst = KMPSearch(patterns[i],data)
        file.write('kmp')        
        file.write(str(i))
        file.write(':')
        mydic = {'type':'kmp','time':tm,'list':lst,'file':'aesop11', 'pattern':patterns[i]}
        file.write(str(mydic))
        file.write(',')

        tm,lst = RabinSearch(patterns[i],data)
        file.write('RabinSearch')        
        file.write(str(i))
        file.write(':')
        mydic = {'type':'RabinSearch','time':tm,'list':lst,'file':'aesop11', 'pattern':patterns[i]}
        file.write(str(mydic))
        file.write(',')

        tm,lst = FiniteAutomatonMatcher(patterns[i],data)
        file.write('FiniteAutomatonMatcher')        
        file.write(str(i))
        file.write(':')
        mydic = {'type':'FiniteAutomatonMatcher','time':tm,'list':lst,'file':'aesop11', 'pattern':patterns[i]}
        file.write(str(mydic))
        file.write(',')

    file.write('}')
    file.close() 


    with open('gulliver.txt', 'r') as myfile:
        data=myfile.read().replace('\n', '')
    # print(patterns)
    file = open('gulliver_result.json','w')
 
    file.write('{   ')
    
    for i in range(0,((int)(len(patterns))-1)):
        # file.write(patterns[i])
    
        tm,lst = NaiveSearch(patterns[i],data)
        file.write('NaiveSearch')        
        file.write(str(i))
        file.write(':')
        mydic = {'type':'NaiveSearch','time':tm,'list':lst,'file':'gulliver', 'pattern':patterns[i]}
        file.write(str(mydic))
        file.write(',')

        tm,lst = KMPSearch(patterns[i],data)
        file.write('kmp')        
        file.write(str(i))
        file.write(':')
        mydic = {'type':'kmp','time':tm,'list':lst,'file':'gulliver', 'pattern':patterns[i]}
        file.write(str(mydic))
        file.write(',')

        tm,lst = RabinSearch(patterns[i],data)
        file.write('RabinSearch')        
        file.write(str(i))
        file.write(':')
        mydic = {'type':'RabinSearch','time':tm,'list':lst,'file':'gulliver', 'pattern':patterns[i]}
        file.write(str(mydic))
        file.write(',')

        tm,lst = FiniteAutomatonMatcher(patterns[i],data)
        file.write('FiniteAutomatonMatcher')        
        file.write(str(i))
        file.write(':')
        mydic = {'type':'FiniteAutomatonMatcher','time':tm,'list':lst,'file':'gulliver', 'pattern':patterns[i]}
        file.write(str(mydic))
        file.write(',')

    file.write('}')
    file.close() 

    with open('hitch2.txt', 'r') as myfile:
        data=myfile.read().replace('\n', '')
    # print(patterns)
    file = open('hitch2_result.json','w')
 
    file.write('{   ')
    
    for i in range(0,((int)(len(patterns))-1)):
        # file.write(patterns[i])
    
        tm,lst = NaiveSearch(patterns[i],data)
        file.write('NaiveSearch')        
        file.write(str(i))
        file.write(':')
        mydic = {'type':'NaiveSearch','time':tm,'list':lst,'file':'hitch2', 'pattern':patterns[i]}
        file.write(str(mydic))
        file.write(',')

        tm,lst = KMPSearch(patterns[i],data)
        file.write('kmp')        
        file.write(str(i))
        file.write(':')
        mydic = {'type':'kmp','time':tm,'list':lst,'file':'hitch2', 'pattern':patterns[i]}
        file.write(str(mydic))
        file.write(',')

        tm,lst = RabinSearch(patterns[i],data)
        file.write('RabinSearch')        
        file.write(str(i))
        file.write(':')
        mydic = {'type':'RabinSearch','time':tm,'list':lst,'file':'hitch2', 'pattern':patterns[i]}
        file.write(str(mydic))
        file.write(',')

        tm,lst = FiniteAutomatonMatcher(patterns[i],data)
        file.write('FiniteAutomatonMatcher')        
        file.write(str(i))
        file.write(':')
        mydic = {'type':'FiniteAutomatonMatcher','time':tm,'list':lst,'file':'hitch2', 'pattern':patterns[i]}
        file.write(str(mydic))
        file.write(',')

    file.write('}')
    file.close() 


    with open('hound-b.txt', 'r') as myfile:
        data=myfile.read().replace('\n', '')
    # print(patterns)
    file = open('hound-b_result.json','w')
 
    file.write('{   ')
    
    for i in range(0,((int)(len(patterns))-1)):
        # file.write(patterns[i])
    
        tm,lst = NaiveSearch(patterns[i],data)
        file.write('NaiveSearch')        
        file.write(str(i))
        file.write(':')
        mydic = {'type':'NaiveSearch','time':tm,'list':lst,'file':'hound-b', 'pattern':patterns[i]}
        file.write(str(mydic))
        file.write(',')

        tm,lst = KMPSearch(patterns[i],data)
        file.write('kmp')        
        file.write(str(i))
        file.write(':')
        mydic = {'type':'kmp','time':tm,'list':lst,'file':'hound-b', 'pattern':patterns[i]}
        file.write(str(mydic))
        file.write(',')

        tm,lst = RabinSearch(patterns[i],data)
        file.write('RabinSearch')        
        file.write(str(i))
        file.write(':')
        mydic = {'type':'RabinSearch','time':tm,'list':lst,'file':'hound-b', 'pattern':patterns[i]}
        file.write(str(mydic))
        file.write(',')

        tm,lst = FiniteAutomatonMatcher(patterns[i],data)
        file.write('FiniteAutomatonMatcher')        
        file.write(str(i))
        file.write(':')
        mydic = {'type':'FiniteAutomatonMatcher','time':tm,'list':lst,'hound-b':'hitch2', 'pattern':patterns[i]}
        file.write(str(mydic))
        file.write(',')

    file.write('}')
    file.close() 

if __name__ == '__main__':
    main()