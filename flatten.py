l = [[1,'a',['cat'],2],[[[3]],'dog'],4,5] 
lnew=[] 
def is_i_list(a): #this function finds the objects which are list
    if type(a)==list:
        return True
def flatten(l): 
    for i in l:
        if is_i_list(i)==True:
            flatten(i)
        else:
            lnew.append(i) # also append each object
flatten(l)
print(lnew)
