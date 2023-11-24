from login_doublets import *
from algo_py import graph,queue

G3 = buildgraph("lexicons/lex_some.txt", 3)

G4 = buildgraph("lexicons/lex_some.txt", 4)
graph.display(G4)
graph.save(G4,"test")
