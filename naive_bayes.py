import sys

def setup():
    global vals
    vals = []
    global c_m_list
    c_m_list = []

def loop():
    while True:
        print "Please make a selection:"
        print "1: Base Classifier\n2: Predictor\n3: Confusion Matrix\n0: Exit"
        choice = raw_input("->")
        if choice == "1":
            base_classifier()
        if choice == "2":
            if len(vals) == 0:
                print "Must run classifier before predictor!\n"
                continue;
            predictor()
        if choice == "3":
            print "Confusion Matrix"
            confusion_matrix()
        if choice == "0":
            print "Goodbye!"
            break;

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
    temp = float(len([x for x in data if x==attr]))/len(data)
    vals.append(temp)
    return temp
    
def likelihood(attr1, attr2, data1, data2):
    if attr1 == "+" or attr1 == "-":
        temp = [x for x, y in zip(data1, data2) if attr1 in x and y==attr2]
    else:
        temp = [x for x, y in zip(data1, data2) if x==attr1 and y==attr2]
    temp = float(len(temp))/len([x for x in data2 if x==attr2])
    vals.append(temp)
    return temp

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

def base_classifier():
    data = []
    tr_dat = read("proj1train.txt")

    tr_genders = gen(1, tr_dat)
    tr_blood_types = gen(2, tr_dat)
    tr_weight = gen(3, tr_dat)
    tr_weight_ord = weight_convert(tr_weight)
    tr_virus = gen(4, tr_dat)
    print "\n"
    print "Prior probability for not virus: ", prior("N", tr_virus)
    print "Prior probability for positive: ", prior("Y", tr_virus)
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
    print "\n"

def discriminator(data):
    #Test the incoming data [id,gender,blood,weight] to guess class
    #Return higher of two discriminators
    if data[1] == "female":
        gender = "f"
    else:
        gender = "m"
    if "+" in data[2]:
        blood = "p"
    else:
        blood = "n"
    if data[3] > 170:
        weight = "y"
    else:
        weight = "n"

    if gender == "f":
        if blood == "p":
            if weight == "y":
                d1  = vals[0] * vals[2] * vals[6] * vals[10]
            else:
                d1 = vals[0] * vals[2] * vals[6] * vals[12]
        else:
            if weight == "y":
                d1 = vals[0] * vals[2] * vals[8] * vals[10]
            else:
                d1 = vals[0] * vals[2] * vals[8] * vals[12]
    else:
        if blood == "p":
            if weight == "y":
                d1 = vals[0] * vals[4] * vals[6] * vals[10]
            else:
                d1 = vals[0] * vals[4] * vals[6] * vals[12]
        else:
            if weight == "y":
                d1 = vals[0] * vals[4] * vals[8] * vals[10]
            else:
                d1 = vals[0] * vals[4] * vals[8] * vals[12]
    
    if gender == "f":
        if blood == "p":
            if weight == "y":
                d2  = vals[1] * vals[3] * vals[7] * vals[11]
            else:
                d2 = vals[1] * vals[3] * vals[7] * vals[13]
        else:
            if weight == "y":
                d2 = vals[1] * vals[3] * vals[9] * vals[11]
            else:
                d2 = vals[1] * vals[3] * vals[9] * vals[13]
    else:
        if blood == "p":
            if weight == "y":
                d2 = vals[1] * vals[5] * vals[7] * vals[11]
            else:
                d2 = vals[1] * vals[5] * vals[7] * vals[13]
        else:
            if weight == "y":
                d2 = vals[1] * vals[5] * vals[9] * vals[11]
            else:
                d2 = vals[1] * vals[5] * vals[9] * vals[13]    

    if d1 > d2:
        return "N"
    else:
        return "Y"

def predictor():
    #Loop through each test data entry and run it through the discriminator
    te_dat = read("proj1test.txt")    
    for x in range(0, len(te_dat)):
        d = discriminator(te_dat[x]);
        print str(x+1) + " " + str(te_dat[x][4]) + " " + str(d)
        save = [te_dat[x][4], d]
        c_m_list.append(save)
    print ""
        

def confusion_matrix():
    tp = 0
    fp = 0
    fn = 0
    tn = 0
    for x in c_m_list:
        if x[0] == "Y":
            if x[1] == "Y":
                tp += 1
            else:
                fn += 1
        else:
            if x[1] == "Y":
                fp += 1
            else:
                tn += 1

    print "\n  |  Y  |  N\n-------------"
    print "Y | " + str(tp).zfill(3) + " | " + str(fn).zfill(3)
    print "N | " + str(fp).zfill(3) + " | " + str(tn).zfill(3) + "\n"
    
                

setup()
loop()
sys.exit
