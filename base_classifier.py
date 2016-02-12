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
    if attr1 == "+" or attr1 == "-":
        res = [x for x, y in zip(data1, data2) if attr1 in x and y==attr2]
    else:
        res = [x for x, y in zip(data1, data2) if x==attr1 and y==attr2]
    return float(len(res))/len([x for x in data2 if x==attr2])

def weight_convert(data):
    res = []
    for x in range(0,len(data)):
        if int(data[x]) > 170:
            res.append("Y")
        else:
            res.append("N")
    return res

def pr_sep():
    print "---------------------------------------------------------------"

tr_dat = read("proj1train.txt")
te_dat = read("proj1test.txt")

tr_genders = gen(1, tr_dat)
tr_blood_types = gen(2, tr_dat)
tr_weight = gen(3, tr_dat)
tr_weight_ord = weight_convert(tr_weight)
tr_virus = gen(4, tr_dat)

print "Prior probability for not virus: ", prior("Y", tr_virus)
print "Prior probability for positive: ", prior("N", tr_virus)
pr_sep()
print "Likelihood for female given not virus: ", likelihood("female", "N", tr_genders, tr_virus)
print "Likelihood for female given virus: ", likelihood("female", "Y", tr_genders, tr_virus)
print "Likelihood for male given not virus: ", likelihood("male", "N", tr_genders, tr_virus)
print "Likelihood for male given virus: ", likelihood("male", "Y", tr_genders, tr_virus)
pr_sep()
print "Likelihood for blood positive given not virus: ", likelihood("+", "N", tr_blood_types, tr_virus)
print "Likelihood for blood positive given virus: ", likelihood("+", "Y", tr_blood_types, tr_virus)
print "Likelihood for blood negative given not virus: ", likelihood("-", "N", tr_blood_types, tr_virus)
print "Likelihood fod blood negative given virus: ", likelihood("-", "Y", tr_blood_types, tr_virus)
pr_sep()
print "Likelihood for weight > 170 given not virus: ", likelihood("Y", "N", tr_weight_ord, tr_virus)
print "Likelihood for weight > 170 given virus: ", likelihood("Y", "Y", tr_weight_ord, tr_virus)
print "Likelihood for weight <= 170 given not virus: ", likelihood("N", "N", tr_weight_ord, tr_virus)
print "Likelihood for weight <= 170 given virus: ", likelihood("N", "Y", tr_weight_ord, tr_virus)


"""
fwv = [x for x, y in zip(tr_genders, tr_virus) if x=="female" and y=="N"]
print float(len(fwv))/len([x for x in tr_virus if x=="N"])
print likelihood("female", "N", tr_genders, tr_virus)

fv = 0
tr_split = []
for x in range(0, len(tr_dat)):
    tr_split.append(tr_dat[x].split(','))

for x in range(0, len(tr_split)):
    if tr_split[x][1]=="female":
        if tr_split[x][4].strip()=="Y":
            fv += 1
"""
