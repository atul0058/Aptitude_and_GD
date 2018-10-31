#dict=dict()
#names=['ankit', 'jala', 'atul', 'jala', 'atul', 'high']
"""
for name in names:
	if name not in dict:
		dict[name]=1
	else:
		dict[name]=dict[name]+1


print(min(dict))
"""
"""
for name in names:
        dict[name]=dict.get(name,0)+1
print(dict)

#this is a very important code for writing a empty dictionary, it adds new keys
#as well as existing keys.

"""
"""
dict[3]='atul'
dict[2]="jala"

print(dict[2])
"""
stuff = dict()
print(stuff)

dict={}
names=['ankit', 'jala', 'atul', 'jala', 'atul', 'high']
for name in names:
        dict[name]=dict.get(name,0)+1
print(dict.keys())
print(dict.values())
print(dict.items())
a=[]
b=[]

"""
name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
dict={}
for line in handle:
    line=line.rstrip()
    if line.startswith('From '):
        a=line.split()
        x=a[1]
        dict[x]=dict.get(x,0)+1
x=None
#print(dict)
for i in dict.values():
    if x<i:
        x=i
    
        
#print(x)
#print(max(dict.values()))

for (k,v) in dict.items():
    if v==5:
        y=k
    
print(y,x)
"""