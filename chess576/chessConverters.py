#these converters could be avoided by hashing (i.e. dictionary structure)

cols = "abcdefgh"

def num2str(coords):
    if not(isinstance(coords,list)) or len(coords)!=2:
        print("not a pair")
        return ""
    for x in coords:
        if not(isinstance(x, int)) or x<0 or x>7:
##            print("invalid coord") #error printing should be in driver
            return ""
    return cols[coords[0]]+str(coords[1]+1)

def str2num(strg): #converts code to (0,0)-(7,7) coords
    if not(isinstance(strg,str)):
        print("not a string")
        return []
    if len(strg)!=2:
        print("len not two")
        return []
    x=strg[0]
    if x.lower() not in cols:
        print("not a valid a-h column")
        return []
    try:
        N=int(strg[1])
    except ValueError:
        print("not a valid 1-8 row")
        return []
    if N>8 or N<1:
        print("not a valid 1-8 row")
        return []
    return [cols.find(strg[0]), N-1]