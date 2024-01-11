'''
Hmm seems like the following strategy is still not
efficient enough. 

The reason is as follows. Suppose I have 9999 1s. 
This will occupy all the spots 
'''
import sys

lines = sys.stdin.readlines()

n = int(lines[0]) # 200k
s = set()
multiple = [1]*10000
for line in lines[1:n+1]:
    c = int(line)
    if c not in s:
        s.add(c)
        multiple[c] += 1
        print(c)
        continue
    else:
        while True:
            if multiple[c]*c not in s:
                s.add(multiple[c]*c)
                print(multiple[c]*c)
                multiple[c]+=1
                break
            else:
                multiple[c]+=1

'''
I want to add 1
multiple[1] = 3

if 3 not in s:
    False
Triggers else:
    multiple[c]+=1
    multiple[c] = 4
if multiple[4] (4) not in s:
    False
Triggers else:
    multiple[c] +=1
    multiple[1] = 5

if 5 not in s:
    s.add(multiple[c])
    multiple[c] +=1
    break


    I want to add 5
multiple[5] = 1

multiple[5] in s
trigger else
multiple[5] += 2
if multiple[c]*c not in s:
        2 *    5  (10)
    s.add(multiple[c]*c)
    multiple[c]+=1
    break
while True:
    if mutiple[c]*c not in s:
        s.add(multiple[c]*c)
        multiple[c]+=1
        break
    else:
        multiple[c]+=1
now 10 is occupied in s
multiple[5] = 3

now I want to add 5 again

5 in s, trigger else

3*5 = 15 not in s
 - add(15)
 -multiple[5] = 4
 break

'''