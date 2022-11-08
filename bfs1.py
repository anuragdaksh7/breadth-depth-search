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
