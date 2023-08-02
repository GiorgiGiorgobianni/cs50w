s = set()

# Add elements to set
s.add(1)
s.add(2)
s.add(3)
s.add(4)
s.add(4)#won't print a duplicate

s.remove(2)#remove element from set

print(s)

print(f"Set has {len(s)} elements")#won't count a duplicate