import sys

def setup():
    global data
    data = []

def loop():
    while True:
        print "Please make a selection:"
        print "1: Base Classifier\n2: Predictor\n3: Confusion Matrix\n0: Exit"
        choice = raw_input("-> ")
        if choice == "1":
            base_classifier()
        if choice == "2":
            predictor()
        if choice == "3":
            print "Chose 3!"
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
    data.append(temp)
    return temp
    
def likelihood(attr1, attr2, data1, data2):
    if attr1 == "+" or attr1 == "-":
        temp = [x for x, y in zip(data1, data2) if attr1 in x and y==attr2]
    else:
        temp = [x for x, y in zip(data1, data2) if x==attr1 and y==attr2]
    temp = float(len(temp))/len([x for x in data2 if x==attr2])
    data.append(temp)
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
#    te_dat = read("proj1test.txt")

    tr_genders = gen(1, tr_dat)
    tr_blood_types = gen(2, tr_dat)
    tr_weight = gen(3, tr_dat)
    tr_weight_ord = weight_convert(tr_weight)
    tr_virus = gen(4, tr_dat)
    print "\n"
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
    print "\n"

def discriminator(data):
    #Test the incoming data [id,gender,blood,weight] to guess class
    #Return higher of two discriminators
    return 0

def predictor():
    #Loop through each te_dat entry and run it through the discriminator
    te_dat = read("proj1test.txt")    
    for x in range(0, len(te_dat)):
        print str(x+1) + " " + str(te_dat[x][4]) + " " + str(discriminator(te_dat[x]))

setup()
loop()
sys.exit
