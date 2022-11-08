"""
  o-----o
 / \    |
o   o   |
 \ /    |
  o-----o
           n1       target
 parent        n2 
          n3          n4
          
parent->n1,n3
n1->n2,target
n2->none
n3->n2,n4
n4->target
"""

nodes = {
}
nodes["target"] = []
nodes["n4"] = ["target"]
nodes["n2"] = []
nodes["n1"] = ["target","n2"]
nodes["n3"] = ["n4","n2"]
nodes["parent"]=["n1","n3"]


def chkKey(key):
	print(key)
	if len(nodes[key]) == 0 and key != "target":
		#print("hmm")
		return
	for i in nodes[key]:
		if i[0] != "target":
			chkKey(i)
		else :
			print("found")
			return
chkKey("parent")
