'''
**Understanding the qn:**
First line contains a recording of all animal sounds. 
next n lines contains all noises made by animals. 

My job, it seems, is to eliminate all known sounds from 
the string, and then what's left over is the sound
of the fox. 

**Initial Problem Analysis:**
First, I have a list of sounds. L1. L1 contains at
most 100 words.

And I also have a second list of known sounds. L2

I want to eliminate L2 from L1, if found. And I 
want to do it efficiently. 

Let's say I have a dict of known sounds. 
d. 

Higher level implementation:
1. Create a dict of known sounds. 
    - key = sound. value = True
2. Iterate through sounds in forest. 
3. If dict[sound] = True, next. 
4. If dict[sound] = '', append to second list. 
5. print second list
'''
from collections import defaultdict

n = int(input())
for _ in range(n):
    knownSounds = defaultdict(lambda: '')
    sounds = input().split()
    foxSounds = []
    while True:
        line = input()
        if line == 'what does the fox say?':
            break
        line = line.split()
        knownSounds[line[-1]] = True
    for sound in sounds:
        if knownSounds[sound] == True:
            continue
        else:
            foxSounds.append(sound)
    print(' '.join(foxSounds))
    