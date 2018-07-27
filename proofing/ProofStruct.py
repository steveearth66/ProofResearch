# first attempt at making a structure to model a proof
# for Jeremy Johnson's CS270 research assistantship
# Author: Steve Earth, ver 1.5, 07/25/18

#for testing: r=rule, a=assume, x=exits (sub)proof, z = undo immediate x
entries = "rrarxraraxzrxrxrx"
#should look like [1 2 [3 4] 5 [6 7 [8 9] 10] 11]
# prooflines = [1 2 2.1 2.2 3 3.1 3.2 3.2.1 3.2.2 3.3 4]
prooflines = []
step=0
prior = -1
for e in entries:
    pass

#determines if first line can access the second; used in rule verification
def access(newline, oldline):
    #shouldn't happen since private call, but just in case...
    if not(isinstance(newline,list)) or not(isinstance(oldline, list)) or \
    newline==[] or oldline==[]:
        return False
    oldL, newL = len(oldline), len(newline)
    if oldL > newL:
        return False
    #this can actually be done in a single case, but harder to follow then
    if oldL == newL: #need all to exactly match until last one which is less
        return oldline[:-1]==newline[:-1] and oldline[-1]<newline[-1]
    #note that in this case the last element could actually be EQUAL!
    return oldline[:-1] == newline[:oldL-1] and oldline[-1]<=newline[oldL-1]

class ProofStep: #comprises elements of the Proof.steps list,
    def __init__(self, expression, justify):
        self.exp = expression #the wff
        self.rule = justify #the rule that justifies that exp
        self.num = [0] #this will be the tuple format used by access function

    def setNum(num):
        self.num = num #tuple to be computed based off entire Proof

class Proof:
    def __init__(self, assumpts, goal):
        self.assumpts = assmpts #a list of wffs
        self.goal = [] #should be final line of steps
        self.steps=[] #should be a list of ProofSteps
        for i in range(len(assupts)):
            self.steps.append(a)
            #FIXME: need to initialize as prior num
            self.steps[i].num.append(i) #starts assumpts as [3,4,0], [3,4,1] etc