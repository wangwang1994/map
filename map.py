list_long=[]
list_lat=[]
with open('long.txt') as f:
    for line in f.readlines():
        line=line.replace('\n','')
        list_long.append(line)
with open('lat.txt') as f2:
    for line in f2.readlines():
        line=line.replace('\n','')
        list_lat.append(line)
list_nox_inlet=[]
with open('nox_inlet.txt') as f3:
    for line in f3.readlines():
        line=line.replace('\n','')
        list_nox_inlet.append(line)
list_nox_outlet=[]
with open('nox_inlet.txt') as f4:
    for line in f4.readlines():
        line=line.replace('\n','')
        list_nox_outlet.append(line)

list_nox_conversion_eff=[]
with open('conversion_eff.txt') as f5:
    for line in f5.readlines():
        line = line.replace('\n', '')
        if line=='#VALUE!':
            line=0
        if line=="#DIV/0!":
            line=0
        line=float(line)
        if line<0:
            line=0
        if line>1:
            line=1
        list_nox_conversion_eff.append(line)



print('---------')
# print(list_long)
# print(len(list_long))
# print(list_lat)
# print(len(list_lat))
# print(list_nox_inlet)
# print(len(list_nox_inlet))
# print(list_nox_outlet)
# print(len(list_nox_outlet))
print(list_nox_conversion_eff)
print(len(list_nox_conversion_eff))
f=open('nox_conversion.txt','w')
for line in list_nox_conversion_eff:
    line=str(line)
    f.write(line)
    f.write('\n')
f.close()