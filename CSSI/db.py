'''
def customBox(width, height):
    box =""
    for i in range(width):
        box = box+ "#"

    for i in range (height):
        print (box)
'''
'''
tbborder= '#########'
lbborder= '##     ##'
for i in range (2):
    print tbborder

for i in range (4):
    print lbborder

for i in range (2):
    print tbborder
'''
'''
tbborder= ' #########'
lbborder= '##     ##'

print ('  123456')
print (tbborder)
for i in range (8):
    print (chr (65 +i) + lbborder)

print (tbborder)
'''
'''
letters = ('A1 A2 A3 A4 A5 A6 A7 A8')
alph =('B1 B2 B3 B4 B5 B6 B7 B8')
print letters
print alph
'''
'''
print "{0} and {1} {2} up the {3}". format ("jack", "jill", "ran", "hill")
'''


info =""
info =("#" * 24) +'\n'
for j in range(8):
    for i in range(1,9):
        info = info + chr(65+j) + str(i)
        if i!= 8:
            info = info + " "

    info = info + '#\n'
info =info + ("#" * 24) + '#\n'
print (info)
