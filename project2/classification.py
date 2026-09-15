from collections import deque 

# --- TASK 1: Create Dataset --- 

 

hastag_n = int(input("Enter the number of hashtags to take: ")) 

hastags_name = [] 

 

for i in range(hastag_n): 

hastags_name.append(input("Enter the name of the hashtag: ")) 

print("\nComplete List of Hashtags:") 

  

for i in hastags_name: 

print(i) 

 

 

# --- TASK 2: Perform Collection Operations --- 

 

print(f"\nThe first hashtag is {hastags_name[0]}") 

print(f"The last hashtag is {hastags_name[-1]}") 

 

print("\nThe first four hashtags using slicing:") 

 

 

for name in hastags_name[:4]: 

print(name) 

print("\nAlternate hashtags:") 

for i in range(0, len(hastags_name), 2): 

print(hastags_name[i]) 

new_hash = input("\nEnter a new hashtag: ") 

hastags_name.append(new_hash) 

rem = input("Enter the hashtag to remove: ") 

if rem in hastags_name: 

hastags_name.remove(rem) 

print("\nUpdated List:") 

for name in hastags_name: 

print(name) 

# --- TASK 3: Stack Implementation (LIFO) --- 

stack = deque() 

n = int(input("\nHow many preprocessing steps? ")) 

for _ in range(n): 

stack.append(input("Enter Preprocessing Step: ")) 

print("\nStack contents:") 

for i in range(len(stack)): 

print(f"Preprocessing step: \t {stack[i]}") 

print(f"The top element of the stack is {stack[-1]}") 

a = stack.pop() 

  

print(f"The popped element is {a}") 

print("\nThe remaining entries in the stack are:") 

for step in stack: 

print(step) 

# --- TASK 4: Queue Implementation (FIFO) --- 

queue = deque()  

cnt = int(input("\nEnter number of post IDs: ")) 

for i in range(cnt): 

queue.append(input("Enter ID: ")) 

 

print("\nQueue contents:") 

for ID in queue: 

print(ID) 

 

print(f"\nThe first element in the queue is {queue[0]}") 

print(f"The last element in the queue is {queue[-1]}") 

a = queue.popleft() 

print(f"The dequeued Post id is {a}") 

 

print("\nUpdated Queue:") 

for ID in queue: 

print(ID) 

# --- TASK 5: Data Science Analysis --- 

 

print("\nDATA SCIENCE REPORT") 

print(f"Total Hashtags: {len(hastags_name)}") 

print(f"Remaining Stack size: {len(stack)}") 

print(f"Remaining Queue size: {len(queue)}") 

 

if len(queue) > len(stack): 

print("High Incoming Data Volume") 

else: 

print("Data Processing is Stable") 

 

# --- TASK 6: Business Recommendation --- 

print("\nBUSINESS RECOMMENDATION") 

  

if len(queue) > 10: 

print("Increase Computing Resources.") 

elif not stack: 

print("Data Preprocessing Completed.") 

else: 

print("Continue Data Cleaning.") 

 