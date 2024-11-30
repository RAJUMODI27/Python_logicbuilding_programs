# Write a Python Program to print the
# output as follows. C
#  CP
#  CPr
# CPro
#  CProg
#  CProgr
#  CProgra
#  CProgram
#  CProgramm
#  CProgrammi
#  CProgrammin
#  CProgramming



word = "CProgramming"

for i in range(1, len(word) + 1):
    print(word[:i])
