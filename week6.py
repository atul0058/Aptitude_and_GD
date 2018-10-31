#tuples and strings are immutable. You can't change them. Where as list are mutable. You can chnage them.

"""
Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.

name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
dict=()
x=[]
for line in handle:
    line=line.rstrip()
    if line.startswith('From '):
        y=line.split()[5].split(':')[0]
        y=str(y)
        x.append(y)
        #print(y)
        #print(line.split()[5].split(':')[0])
       
#print(x)
dict={}
for y in x:
    dict[y]=dict.get(y,0)  +1
#print(dict)
lst=[]
for (k,v) in dict.items():
    newtup=(k,v)
    lst.append(newtup)
    
lst=sorted(lst)
for (k,v) in lst:
    print(k,v)
    