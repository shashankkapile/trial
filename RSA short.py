
# coding: utf-8

# In[1]:


def gcd(phiN,e):
    remain=phiN%e
    if(remain==0 ):
        return e
    else:
        return gcd(e,remain)
    

def getE(phiN):
    list=[]
    for e in range(3,phiN-1):
        if(gcd(phiN,e)==1):
            list.append(e)
    print(list)
    
def getD(phiN,e):
    i=1
    while(True):
        d=((phiN*i)+1)/e
        if int(d)==d:
            return d
        i=i+1
    


# In[11]:


a,b=13,11
phiN=(a-1)*(b-1)
N=a*b
# print(gcd(7,4))
getE(phiN)
e=int(input("Select an e: "))
d=int(getD(phiN,e))
# gcd(7,3)
# e


# In[14]:


print("a= "+str(a)+" b= "+str(b)+" N= "+str(N)+" phiN= "+str(phiN)+" e= "+str(e)+" d= "+str(d))
print(str(e)+" "+str(N))
print(str(d)+" "+str(N))

#this is single character plain text
plain=13

c= (plain **e)%N
print(c)
p=(c**d)%N
print(p)

'''
p,q=17,7
a,b=5,3
r=(q**a)%p
s=(q**b)%p

rk=(s**a)%p
print(rk)'''

