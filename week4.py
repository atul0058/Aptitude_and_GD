atul='string'
print(atul[1])
print("-----")
for i in atul:
    print(i)
print("-----")

atul1="after three hours you will hop in a bus which will be going to Amsterdam"

x=atul1.split() #this returns a list. Always remember, the split funciton gives you a string

print(x)

print("-----")

#line.rstrip vs line.split()
#line.rstrip removes the \n line where as the line.split() removes the gap between
#the words. The former works on removing the spaces between the lines, while the latter works on removing
#the spaces between the words

#if you want to chop between spaces use line.split()
#if you want to chop between some specail character then use line.split(':')

"""
Open the file romeo.txt and read it line by line. For each line, split the line into a list of words using the split() method. The program should build a list of words. For each word on each line check to see if the word is already in the list and if not append it to the list. When the program completes, sort and print the resulting words in alphabetical order.
You can download the sample data at http://www.py4e.com/code3/romeo.txt

fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    line=line.rstrip()
    for x in line.split():
        if x not in lst:
        	lst.append(x)
lst.sort()    
print(lst)

"""

"""
Open the file mbox-short.txt and read it line by line. When you find a line that starts with 'From ' like the following line:
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
You will parse the From line using split() and print out the second word in the line (i.e. the entire address of the person who sent the message). Then print out a count at the end.
Hint: make sure not to include the lines that start with 'From:'.
fname = input("Enter file name: ")
if len(fname) < 1 : 
    fname = "mbox-short.txt"
fh = open(fname)
count=0
lst=[]
for line in fh:
    line.rstrip()
    if line.startswith('From '):
        z=line.split()
        z1=z[1]
        lst.append(z1)
        count=count+1
            
for i in lst:
    print(i)
    
print("There were", count ,"lines in the file with From as the first word")  
       
"""


You can download the sample data at http://www.py4e.com/code3/mbox-short.txt




