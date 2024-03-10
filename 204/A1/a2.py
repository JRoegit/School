
# This is your unique solution file

from config import *
from lib204 import semantic_interface

# Assignment for 21JNR6

# Note: All of these answers are almost certainly wrong

a2q12 = [ [s1],[s2,s3,s4] ]

a2q13 = {
    P: True,
    T: True,
    R: False
}

a2s5nnf = [
    [((S&(Q|P))>>~(Q|~P)), 'starting formula'],
    [~(S&(Q|P))|~(Q|~P), 'replace implications'],
    [(~S|~(Q|P)|(~Q&P)), 'de Morgans'],
    [(~S|(~Q&~P)|(~Q&P)), 'de Morgans'],
]

a2s6nnf = [
    [((P>>~(Q|~S))|(Q&~S)), 'starting formula'],
    [~P|~(Q|~S)|(Q&~S), 'replace implications'],
    [~P|(~Q&S)|(Q&~S), 'de Morgan'],
]

a2s5cnf = [
    [((S&(Q|P))>>~(Q|~P)), 'starting formula'],
    [~(S&(Q|P))|~(Q|~P), 'replace implications'],
    [~S|~(Q|P)|(~Q&P), 'de Morgans'],
    [~S|(~Q&~P)|(~Q&P), 'de Morgans']
    [(~S|~Q)&(~S|~P)|(~Q&P), 'distribution']
    [((~S|~Q)|(~Q&P))&(~S|~P)|(~Q&P), 'distribution']
    [(((~S|~Q)|~Q)&((~S|~Q)|P))&(((~S|~P)|~Q)&((~S|~P)|P)), 'distribution']
    [(~Q|~S)&(~P|~S|~Q), 'simplify']
]

a2s6cnf = [
    [((P>>~(Q|~S))|(Q&~S)), 'starting formula'],
    [(~P|~(Q|~S))|(Q&~S), 'replace implications'],
    [(~P|(~Q&S))|(Q&~S), 'de Morgans']
    [((~P|~Q)&(~P|S))|(Q&~S), 'distribution']
    [(((~P|~Q)&(~P|S))|Q)&(((~P|~Q)&(~P|S))|~S), 'distribution']
    [(((~P|~Q)|Q)&((~P|S)|Q))&(((~P|~Q)|~S)&((~P|S)|~S)), 'distribution']
    [(S|~P|Q)&(~Q|~P|~S), 'simplify']
]

a2s5tseitin = semantic_interface.Encoding()
# Fill in the Tseitin steps and finalize
x1 = a2s5tseitin.tseitin(P, 'x1') # just an example
x2 = a2s5tseitin.tseitin(~x1, 'x2')
x3 = a2s5tseitin.tseitin(Q | x2, 'x3')
x4 = a2s5tseitin.tseitin(~x3, 'x4')
x5 = a2s5tseitin.tseitin(Q | P, 'x5')
x6 = a2s5tseitin.tseitin(x5 & S, 'x6')
x7 = a2s5tseitin.tseitin(x6 >> x4, 'x7')
a2s5tseitin.finalize(x7) # make sure you update the variable!

a2s6tseitin = semantic_interface.Encoding()
# Fill in the Tseitin steps and finalize
x1 = a2s6tseitin.tseitin(S, 'x1') # just an example
x2 = a2s5tseitin.tseitin(~x1, 'x2')
x3 = a2s5tseitin.tseitin(x2 | Q, 'x3')
x4 = a2s5tseitin.tseitin(~x3, 'x4')
x5 = a2s5tseitin.tseitin(P >> x4, 'x5')
x6 = a2s5tseitin.tseitin(Q & x2, 'x6') # Re use x2 here as it exists already
x7 = a2s5tseitin.tseitin(x5 | x6, 'x7')
a2s6tseitin.finalize(x7) # make sure you update the variable!

