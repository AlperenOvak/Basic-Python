l =[[1, 2], [3, 4], [5, 6, 7]]
l=l[::-1] #reverse the maiin list

for i in range(len(l)):
    (l[i])=(l[i])[::-1] #reverse the lists which are the objects of the main list
print(l)