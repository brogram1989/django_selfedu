# s = '()[]{}'
# el = [ s[i] for i in range(len(s)) ]
# for i in reversed(range(len(el))):
#     print(i)
#
#




a = [1,3,5]
b = [2,4 ]

for i in range(len(b)):
    a.append(b[i])
print(a)
aa = sorted(a)
if (len(aa)%2 == 0):
    median = (aa[int(len(aa)/2) + 1] + aa[int(len(aa)/2) - 1])/2
else:
    median = (aa[int(len(aa)/2)])

print(aa, median)





