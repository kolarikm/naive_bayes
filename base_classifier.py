#import lib

def read(fname):
    with open(fname) as f:
        temp = f.readlines()
    res = []
    for x in range(0, len(temp)):
        res.append([y.strip() for y in temp[x].split(',')])
    return res

def gen(attr, data):
    res = []
    for x in range(0,len(data)):
        res.append(data[x][attr])
    return res

def prior(attr, data):
    return float(len([x for x in data if x==attr]))/len(data)

def likelihood(attr1, attr2, data1, data2):
    res = [x for x, y in zip(data1, data2) if x==attr1 and y==attr2]
    return float(len(res))/len([x for x in data2 if x==attr2])
    

tr_dat = read("proj1train.txt")
te_dat = read("proj1test.txt")

tr_genders = gen(1, tr_dat)
tr_blood_types = gen(2, tr_dat)
tr_weight = gen(3, tr_dat)
tr_virus = gen(4, tr_dat)

print "Prior probability for virus-negative: ", prior("Y", tr_virus)
print "Prior probability for virus-positive: ", prior("N", tr_virus)

fwv = [x for x, y in zip(tr_genders, tr_virus) if x=="female" and y=="N"]
print float(len(fwv))/len([x for x in tr_virus if x=="N"])
print likelihood("female", "N", tr_genders, tr_virus)

"""
fv = 0
tr_split = []
for x in range(0, len(tr_dat)):
    tr_split.append(tr_dat[x].split(','))

for x in range(0, len(tr_split)):
    if tr_split[x][1]=="female":
        if tr_split[x][4].strip()=="Y":
            fv += 1
"""
