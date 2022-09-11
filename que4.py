"""
Input:
data=[{"camp":1,"bid":1}, {"camp":1,"bid":2}, {"camp":2,"bid":3}, {"camp":2,"bid":4}, {"camp":3,"bid":5}]

Output:

OUTput Should be
[{'camp': 1, 'bid': [1, 2]}, {'camp': 2, 'bid': [3, 4]}, {'camp': 3, 'bid': [5]}]

"""

data=[{"camp":1,"bid":1}, {"camp":1,"bid":2}, {"camp":2,"bid":3}, {"camp":2,"bid":4}, {"camp":3,"bid":5}]

l1 = data[0::2]
l2 = data[1::2]

from collections import defaultdict

temp = defaultdict(list)

for elem in l1:
    temp[elem['camp']].append(elem['bid'])
  
for elem in l2:
    temp[elem['camp']].append(elem['bid'])
  
Output = [{"camp":x, "bid":y} for x, y in temp.items()]
  
print(Output)