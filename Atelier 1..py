"""
Nom et prénom : Karim Serroukh Youness
APOGEE : 16004087
CNE : P141043309
"""

# Question (1):
print("Question 1 :")
l1=[3,6,9,12,15,18,21]
l2=[4,8,12,16,20,24,28]
l3=[]
for i in range(0,len(l1)):
    if i%2==1:
        l3.append(l1[i])
for i in range(0,len(l2)):
    if i%2==0:
      l3.append(l2[i])
print(l3)

# Question (2):
print("Question 2 :")

mylist = [11, 45, 8, 23, 14, 12, 78, 45, 89]
a = []
b = []
c = []
for i in range (0, int(len(mylist)/3)):
    a.append(mylist[i])
    b.append(mylist[i + (len(mylist)//3)])
    c.append(mylist[i + (2 * (len(mylist)//3))])

print(a[::-1], b[::-1], c[::-1])

# Question (3):
print("Question 3 :")

mylist=[11, 45, 8, 11, 23, 45, 23, 45, 89]
def occurence(mylist,n):
    occu=0
    for el in mylist:
        if el==n:
            occu+=1
    return occu


mydict = {}

for i in range(len(mylist)):
    mydict[mylist[i]] = occurence(mylist, mylist[i])

print(mydict)


# Question (4):
print("Question 4 :")

myset1 = {23, 42, 65, 57, 78, 83, 29}
myset2 = {57, 83, 29, 67, 73, 43, 48}

inter = myset1.intersection(myset2)
print(f" L'intersection des deux sets est : {inter}")

for el in inter:
    myset1.remove(el)
print(f"Set 1 après suppression : {myset1}")


# Question (5):
print("Question 5 :")

mylist=[47, 64, 69, 37, 76, 83, 95, 97] 
mydict={'Yassine':47, 'Imane':69, 'Mohammed':76, 'Abir':97}

for el in mylist.copy():
    if el not in (mydict.values()):
        mylist.remove(el)
print(mylist)