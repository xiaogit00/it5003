"""
If this problem is too difficult, why not try to do the simplest version of this problem?

Like, look. I am just going to write a program that fills shelves. I don't care if the number of shelves needed is the least. 

And the method I am going to fill the shelves is simple. I will begin with the large books first. I'll fill up the entire shelf as much as I can. Then, I'll proceed to try to fill with the m books. I'll fill it with m books as much as I can. Then, I'll fill with the s books, until the shelf is full. If I cannot fill with the s books, or if the filled == w at any point, this shelf is filled, and I'll take the remainer books and try to fill the next shelf in the same way. 

Break down the higher level logic: 
1. Check for L books
2.  Try to fill shelf with as many large books as possible. -> if filled ==w, break
3. Check for m books 
4. Fill with m books -> if filled ==w, break
5. Check for s books
6. Fill with s books. -> if filled ==w, break
7. get remainingbooks
8. Fill the next shelf with the same logic, until all 3 are 0

Let S, M, L be the number of small, medium, large books we have. 
Let s, m, l be the width of the small, medium, large books

Pseudocode: 
1. As long as there's S, M, or L books:
    2. Check whether first shelf fits 1 large book and that large book exist. If it does, fill first shelf with 1 large book. 
    3. Continue Step 2, until shelf 1 cannot fit large book anymore. Then, check whether shelf is filled. If it is, shelf+1 and continue to next while loop. Else:
       4. Repeat steps 2 and 3 with medium books
            5. Repeat steps 2 and 3 with small books
"""
s, m, l = 1, 2, 3

S, M, L = map(int, input().split())

w = int(input())

shelf = 1

while S > 0 or M > 0 or L > 0:
    filled = 0
    while filled + l <= w and L:
        filled+=l
        L-=1
    if filled == w: # Check if it's filled
        # print(f"Shelf {shelf} filled up")
        shelf+=1
        continue
    else: # If it's not filled,
        # Try to fill with medium books
        while filled + m <= w and M:
            filled +=m 
            M-=1
        if filled == w: # Check if it's filled
            # print(f"Shelf {shelf} filled up")
            shelf+=1
            continue
        else: # If it's not filled,
            # Try to fill with small books
            while filled + s <= w and S:
                filled +=s 
                S-=1
            if filled == w: # Check if it's filled
                # print(f"Shelf {shelf} filled up")
                shelf+=1
                continue
            else:
                # print(f"Shelf {shelf} not filled up, remaining: {w-filled}")
                shelf+=1
          
print(shelf-1)
