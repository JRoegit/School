
# DO NOT EDIT

# Assignment for 21JNR6

from lib204 import wff
P, Q, R, S, T = map(wff.Variable, 'PQRST')
s1 = ((P|T)&R)
s2 = ((~T&R)>>P)
s3 = (~R|(P|T))
s4 = ((~R&~T)|((~P&~T)>>~R))

s5 = ((S&(Q|P))>>~(Q|~P))
s6 = ((P>>~(Q|~S))|(Q&~S))
