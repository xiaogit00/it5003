'''
Instructions: 
F: The mic holder will pass the mic to the person in front of them. It is guaranteed that such a person exists.

B: The mic holder will pass the mic to the person behind them. It is guaranteed that such a person exists.

R: The mic holder will pass the mic to the person behind them. Then, they will move to the back of the line. In the case that the mic holder is at the back of the line, the mic will be passed to the person at the front of the line instead.

C: The mic holder will pass the mic to the person behind them. Then, they will move to behind where their partner is standing. In the case that the mic holder is at the back of the line, the mic will be passed to the person at the front of the line instead.

P: The mic holder will yell their partner’s name into the mic.

Levels
1. No P, R, C instructions
2. No R, C instructions
3. No C type instructions, N<100, Q<500
4. No C type instructions, N<1000, Q<3000
5. No C type instructions
6. N<1000, Q<3000
7. No constraints

PBBPFP

BRBPRFFPRBBBBBRPCBBCFP

Requirements:
1. Print out names yelled
2. Print out the names of person in the line from front to back 

Initial Problem Analysis:
1. It seems like the mic can be a pointer. This pointer will be following a series of instructions. 
2. At certain instructions, it'll be modifying the list. In particular, R will move the person to back of line (append operation?) and C will move them behind their partners (hmm - partners might not be together) - I might need a dictionary to store their partners' names? Need it as well during yelling?.
3. Then at the end, print out the sequence of line. 

I mean, it does seem relatively straightforward to understand, but doing it efficiently is what I'll need to think about. 

So let's consider the kinds of operations. R is a delete instruction, along with an append instruction. This definitely calls for a linked list. If use python array, one delete operation on 5M items will be v expensive. Whereas using linkedList, nothing needs to shift. On top of that, R is also an append instruction. 

C is where a lot of the heavy lifting is. 
1. First, you'll need to fetch their partners from the dictionary. 
2. Then, find their partner's positions in the array (how to make this efficient? should each node store the positions of their partners?)
3. Then, delete from current position
4. Insert at partner's position. -> so if I already have the position of the partner, then it'll be pretty light right? Let's see. Let me progress down the various level first. 

Higher level implementation
1. Create a LinkedList data structure first. 
2. Consume the inputs properly
3. Implement instruction handling: - for F and B first. 
4. Test out with a couple of cases 
'''