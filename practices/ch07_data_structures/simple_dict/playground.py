# Data Structures
# 1. Dictionaries
# 2. Lists / arrays [1.1.7.11]
# 3. Sets

# Dictionaries: Define a key to find a value quickly
# d = dict() works as well as d = {}
# You can create a populated dict() as well
d = {
    'bob': 0,
    'sarah': 0,
    'defeated by': {'paper', 'dynamite'},
    'defeats': {'scissors'}
}

print(d['bob'])
d['bob'] += 1
print(d['bob'])
print(d)
d['russell'] = 7
print(d)
print(f"You are defeated by {d['defeated by']}")
print(d.get('other', 42))

# Lists: Keep elements in order and access them
lst = [1, 7, 1, 11]
print(lst)
lst.append(2)
print(lst)
lst.remove(11)
print(lst)
lst.sort()
print(lst)

# Sets: Check for distinct elements
st = {1, 1, 11, 7}
st.add(1)
st.add(1)
st.add(1)
st.add(11)
print(st)

# Create a dictionary:
d = dict(bill=2, zoe=7, michael=4) # or d = {'bill': 2, 'zoe': 7, 'michael': 4}

# Access the value by key:
name = 'zoe'
print(f"Wins by {name} are {d[name]}")

# Safer access:
wins = d.get(name)
if wins:
    print(f"There are {wins} wins.")
else:
    print (f"{name} has never won a game.")

