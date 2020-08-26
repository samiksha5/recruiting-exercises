order = { 'apple': 5, 'banana': 5, 'orange': 5 };
inv = [ { 'name': 'owd', 'inventory': { 'apple': 5, 'orange': 10 }}, { 'name': 'dm', 'inventory': { 'banana': 5, 'orange': 10 } } ] 

result=[]
fount = []

for key, value in order.items():
  #print(key, value)
  req = value
  flag = 0
  # to go throught all the inventories
  for invent in inv:
    inv_name = invent['name']
    # to go through all the items in inventory 
    if_filled = 0
    for i, j in invent['inventory'].items():
      if i==key:
        if j>=req:
          result.append({inv_name: {i:j}})
          flag = 1
          if_filled = 1
          break
        elif j< req:
          req-=j
         
    if if_filled == 1:
      break
  if flag==0:
    print(' ')
print(result)

'''
output : [{'owd': {'apple': 5}}, {'dm': {'banana': 5}}, {'owd': {'orange': 10}}]

If an order can be completely shipped from one warehouse or shipped from multiple warehouses, which option is cheaper? We can assume that shipping out of one warehouse is cheaper than shipping from multiple warehouses.
for this test case :
order = { 'apple': 5, 'banana': 5, 'orange': 5  };
inv = [ { 'name': 'owd', 'inventory': { 'apple': 5, 'orange': 2 }}, { 'name': 'dm', 'inventory': { 'banana': 5, 'orange': 10 } } ] 

output : [{'owd': {'apple': 5}}, {'dm': {'banana': 5}}, {'dm': {'orange': 10}}]
'''
