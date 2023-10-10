'''
Participants tracked to see if they're infected by 3 different strains of a virus. 

Efficacy of the vaccine against *particular strain* is the % reduction of the infection rate of vaccinated group compared to control group. 

Variables:
infection_rate_A = 0.2
infection_rate_B = 0.6
vaccine_efficacy = (infection_rate_B - infection_rate_A)/infection_rate_B

10
NYNY
NNYY
NYYY
NYYN
NNNY
YYNN
YYYN
YYNY
YYNN
YYNY

The ones that start with N are the control group. Y = vacinnated group. 
Infected with strains A, B, or C. 

At least 1 participant in control group infected by each strain (so won't divide by 0)

I'll need to find vaccine efficacy against strains A, B, or C. 

Ok. so each column is a dataset. so for instance for A:
Control: 3 infected
Vaccinated: All infected. A is not effective. 

For B: 
Control: 3
Vaccinated: 1

Okay now I get it. 

Basically the pseudocode:
For each strain, 
1. Sum up the control column, find the infectedCountC
2. Sum up the vaccinated column, find the infectedCountV.
3. take infectedCountC-infectedCountV/infectedCountC -> that's your efficacy in decimal percentage. 

Implementation:
data = []
an array of items

'''

import sys 

n = 0
data = []
for i, line in enumerate(sys.stdin):
    if 'q' == line.rstrip():
        break
    line = line.rstrip()
    if i == 0:
        n = int(line.rstrip())
    else: 
        data.append(line.rstrip())

for i in range(1, 4): # Loop over 3 strains, in the indices of data[0]
    controlInfectedCount = 0
    vaccinatedInfectedCount = 0
    for line in data:
        if line[0] == 'N': # Control group
            if line[i] == 'Y': controlInfectedCount+=1
        else: # Vaccinated group 
            if line[i] == 'Y': vaccinatedInfectedCount+=1
    print("Not Effective") if vaccinatedInfectedCount >= controlInfectedCount else print((controlInfectedCount-vaccinatedInfectedCount)*100/controlInfectedCount)

# infection_rate_A = 0.2
# infection_rate_B = 0.6
# vaccine_efficacy = (infection_rate_B - infection_rate_A)/infection_rate_B
