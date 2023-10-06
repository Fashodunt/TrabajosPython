tupla = 1,3,4,5,6,7,12,34,67,8,89,56,14
def mid():
    if (len(tupla) % 2 == 0):
        x = len(tupla) // 2
        media = ((tupla[x]),)
        return(media)
    else:
        x = len(tupla)//2
        media = ((tupla[x]),tupla[x+1])
        return(media)
    
midtu = (mid())
print(tupla)
print(midtu)