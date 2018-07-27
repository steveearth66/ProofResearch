# unit testing for most functions
# for Jeremy Johnson's CS270 research assistantship
# Author: Steve Earth, ver 1.5, 07/25/18

import unittest
from proofchecker import *
from ProofStruct import *

pandf = [sand, ["P"], [sfalse]]
notpf = [snot, pandf]
ifqthennotpf = [simply, ["Q"], notpf]
dupes = [snot, [sor, ["T"], [sor, ["P"], ifqthennotpf]]]
parenExp = "(b or {c or d} or (e or a) or (f or (g or h)) or (i or {j or k}) "\
"or {l or (m or n)} or {p or {q or r}} or s) or t"

class TestStuff(unittest.TestCase):
    def test_vars(self):
        yes = ["And","P"]
        no = [sand,"T", 5, True, "5A", "", "p and q"]
        for i in yes:
            self.assertTrue(isVar(i))
        for j in no:
            self.assertFalse(isVar(j))

    def test_wff(self):
        yes = [[sfalse], ["P"],[sand, ["P"], ["Q"]],[snot, ["P"]]]
        no = [[], [""],[sand],[snot, ["P"], ["Q"]]]
        for i in yes:
            self.assertTrue(wellFormed(i))
        for j in no:
            self.assertFalse(wellFormed(j))

    def test_gvars(self):
        self.assertEqual(getVars(["T"]),[])
        self.assertEqual(getVars(["P"]),["P"])
        self.assertEqual(getVars(5),[])
        self.assertEqual(getVars([]),[])
        self.assertEqual(getVars([""]),[])
        self.assertEqual(getVars(dupes),["P","Q"])

    def test_grabGrp(self): #testing consec and also nested paren variants
        trial = preproc(parenExp)
        self.assertEqual("".join(grabGrp(trial)[0]),\
        "b"+sor+"{c"+sor+"d}"+sor+"(e"+sor+"a)"+sor+"("+sfalse+sor+"(g"+sor+\
        "h))"+sor+"(i"+sor+"{j"+sor+"k})"+sor+"{l"+sor+"(m"+sor+"n)}"+sor+"{p"+\
        sor+"{q"+sor+"r}}"+sor+"s")
        self.assertEqual(trial[grabGrp(trial)[1]-1],")")

    def test_cleanUp(self):
        trials =["(((not {<(! {{( - bob)}})>})))", \
        "(((p and -{q})) implies ((!f)))"]
        solns = [snot+snot+snot+"bob", \
        "(p "+sand+" "+snot+"q) "+simply+" "+snot+sfalse]
        for i in range(len(trials)):
            self.assertEqual(cleanUp(trials[i]), solns[i])

    def test_access(self):
        mainline = [5,3,9,4]
        yes1 = [[5],[4],[5, 2],[5, 3], [5,3,9,3]]
        no1=[[6],[5,4],[],0,"",[5,3,9,4],[5,3,9,5], [5,3,9,4,1]]
        yes2 = [[5,3,9,5], [5,3,9,4,1]]
        no2=[[5],[4],[6],[5, 2],[5, 3],[5,4],[],0,[5,3,9,3],"",[5,3,9,4]]
        for i in yes1:
            self.assertTrue(access(mainline, i))
        for j in no1:
            self.assertFalse(access(mainline, j))
        for i in yes2:
            self.assertTrue(access(i, mainline))
        for j in no2:
            self.assertFalse(access(j, mainline))

unittest.main()