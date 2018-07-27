# first attempt at making a logical expression parser/deparser
# for Jeremy Johnson's CS270 research assistantship
# Author: Steve Earth, ver 1.5, 07/25/18

#FIXME: order of operations: (), !, ^, v, ->
#by scan through in 4 passes in !^v-> order and insert () after preproc
#will need a backwards grabGrp that takes a RIGHT and returns index of LEFT

from string import ascii_letters as alphas

# naming some categories to iterate over later
#and/or/not/imply. XOR/IFF?
Operator = [sand, sor, snot, simply] =["\u2227", "\u2228", "\u00AC", "\u2192"]
sfalse = "\u22a5"
Constant = ["T", sfalse]
TRUEs = ["T","t", "True", "TRUE", "true"]
FALSEs = [sfalse,"F", "f", "False", "FALSE", "false"]
ANDs = [sand,"&", "&&", "and", "AND", "And", "^", "*", "."]
ORs = [sor,"v", "V", "|", "||", "OR", "Or", "or", "+"]
NOTs = [snot,"Not", "NOT", "not", "-", "~","!"]
IFs = [simply,"implies", "Implies", "IMPLIES", "THEN", "Then", "then",\
"->", "\u21d2"] # u21d2 is doublearrow, can't display horseshoe symbol \u2283

#double symbols omitted for now and are dealt with in the preproc function
Symbols =[sfalse,sand,sor, snot,simply, "\u2192","&", "^", "*", ".", "v", "V",\
"|", "+","-","~","!","->", "(", ")","{","}", "[", "]","<",">"]
RIGHTs=[")","}",">","]"]
LEFTs=["(","{","<","["]
twin={}
for i in range(4):
    twin[LEFTs[i]]=RIGHTs[i]
    twin[RIGHTs[i]]=LEFTs[i]
symb={} #making dictionary to have consistent symbols
ALLs = [TRUEs, FALSEs, ANDs, ORs, NOTs, IFs]
flatAll = [sym for cat in ALLs for sym in cat]
for a in ALLs:
    for x in a:
        symb[x]=a[0]

def preproc(strg): #converts string into a list with unique op symbols
    if not(isinstance(strg, str)):
        return []
    while "&&" in strg or "||" in strg or "->" in strg:  #handles 2x symbols
        strg = strg.replace("&&","&")
        strg = strg.replace("||", "|")
        strg = strg.replace("->", simply) #avoids ambiguity with negation
    for x in Symbols:
        strg = strg.replace(x, " "+x+" ") #this treats any letter v as an OR!
    strg = strg.split()
    a = [c if c not in flatAll else symb[c] for c in strg]
    return a

def isVar(strg): #var must be a string, start with letter and not be an op/cons
    if not(isinstance(strg, str)) or len(strg)==0 or \
    strg[0] not in alphas or " " in strg: #after tokenizing, " " check moot
        return False
    return not((strg in Operator) or (strg in Constant))

def grabGrp(expList):
    if not(isinstance(expList, list)) or len(expList)==0:
        return []
    if expList[0] not in LEFTs and isVar(expList[0]):
        return [[expList[0]], 1]
    grping={} #counter for the parens, +1 each Left, -1 each Right
    for x in LEFTs:
        grping[x]=0
    startSym = expList[0]
    grping[startSym]=1
    terminator = twin[startSym]
    for i in range(1,len(expList)):
        newSym = expList[i]
        if newSym not in LEFTs+RIGHTs:
            continue
        if newSym in LEFTs:
            grping[newSym]+=1
        if newSym in RIGHTs:
            opp = twin[newSym]
            if grping[opp]==0:
                return [] #right close without left present
            if grping[opp]>1:
                grping[opp]-=1
            elif newSym==terminator:
                return [expList[1:i], i+1] #note i+1 might be beyond expList!
    #if all the way through For loop w/o a Return break,then it never closed
    return []

def remXtraParen(expList): #takes list and pares away any extraneous outer (())
        if not(isinstance(expList, list)) or len(expList)==0:
            return []
        if expList[0] not in LEFTs:
            return expList
        ans = grabGrp(expList)
        if ans==[]:
            print("mismatched parentheses")
            return []
        [trial,ind] = ans
        if ind == len(expList):
            return remXtraParen(trial)
        return expList

#no order hierarchy for operations besides grping. Right always beats Left
#e.g. "p*q@r" will be "p*(q@r)" regardless of */@. o/w use "(p*q)@r"
def makeNested(myList): #converts preproc list into wff list (prove with CoQ?)
    expList = remXtraParen(myList)
    if expList==[]:
        return []
    if len(expList)==1:
        if expList[0] in Constant or isVar(expList[0]):
            return expList
        else:
            return []
    if expList[0]==snot: # negation
        return [snot, makeNested(expList[1:])]
    if expList[0] not in LEFTs and not(isVar(expList[0])): #neg handled above
        return [] #can't start off with an operation other than NOT
    [op1, ind] = grabGrp(expList)
    # op1 = remXtraParen(op1) #not needed since happens when recurse on makeNest
    if ind+1==len(expList): #not well formed since you ended with an operation
        return []
    op2=expList[ind+1:]
    return [expList[ind], makeNested(op1), makeNested(op2)]

#given a list that starts with a ({<[ extracts sublist between matching ]>})
#and returns tuple of that sublist, and index of next part of list (poss OoB)
def converter(expList): #takes preproc list and converts to wff list
    if len(expList)==0:
        return []
    startSym = expList[0]
    if len(expList)==1:
        if startSym in Constant or isVar(startSym):
            return expList
        else:
            return [] #returns null list if not wff
    else:
        if startSym ==snot: #negation
            return [snot, converter(expList[1:])]
        #FIXME: need to scan to find op, it won't be at start of list
        if startSym in [sand, sor, snot]:
            if len(expList)<2:
                return []
            else:
                return [startSym, converter(expList[1]), converter(expList[2])]

def wellFormed(sent): #tells if sent (must be a list!) is well-formed or not
    if not(isinstance(sent, list)) or len(sent)==0:
        return False
    if len(sent)==1: #this means P and "P" are not wff, but ["P"] is.
        return (sent[0] in Constant) or isVar(sent[0])
    if sent[0] not in Operator:
        return False
    if sent[0]==snot:
        if len(sent)!=2:
            return False
        else:
            return wellFormed(sent[1])
    else:
        if len(sent)!=3:
            return False
        else:
            return wellFormed(sent[1]) and wellFormed(sent[2])

#not needed for parsing
def getVars(sent):
    if not(wellFormed(sent)) or sent[0] in Constant:
        return []
    if isVar(sent[0]):
        return [sent[0]]
    if sent[0]==snot:
        return getVars(sent[1])
    ans = getVars(sent[1])
    addins = getVars(sent[2]) #insures no duplicates in variable list
    for x in addins:
        if x not in ans:
            ans.append(x)
    return ans

#takes a wff and returns natural English string
def deParser(wff):
    if not(wellFormed(wff)):
        return "not a well formed expression"
    if len(wff)==1:
        return wff[0]
    if wff[0] ==snot:
        if wff[1][0] in Constant or isVar(wff[1][0]) or wff[1][0]==snot:
            return snot+deParser(wff[1]) #don't need to create parens
        return snot+"("+deParser(wff[1])+")" #not wff[1:] since nested!
    ans = []
    for i in range(1,3):
        if wff[i][0] in Constant or isVar(wff[i][0]) or wff[i][0]==snot:
            ans.append(deParser(wff[i]))
        else:
            ans.append("("+deParser(wff[i])+")")
    return ans[0]+" "+wff[0]+" "+ans[1]

#pretty print!!
def cleanUp(strg):
    return deParser(makeNested(preproc(strg)))