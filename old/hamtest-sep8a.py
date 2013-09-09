#!/usr/bin/python2.7
#
# this will be a complete rewrite of hamtestprep in pythion 2.x

f = open('dos2unix.out', 'r')
file = f.readlines()
questionid = ["",]
qnum = 0
qanswerkey = ["",]

for n in range(0,2816):
    # Get QuestionID
    if file[n] == "~~\n":
    #if file[n-6] == "":
    #  questionid[qnum:] = [file[n-5][0:5]
    #  qnum = qnum + 1
    #  print questionid[qnum -1]
    #  continue
        questionid[qnum:] = [file[n-6][0:5]]
        qanswerkey[qnum:] = re.sub(r'.*\(|\).*','',[file[n-6]])
    print file[n]
    print questionid[qnum:]
    print questionid[qnum]
    if questionid[qnum] == '\n':
        questionid[qnum:] = [file[n-5][0:5]]
        qanswerkey[qnum:] = re.sub(r'.*\(|\).*','',[file[n-5]])
# TODO: add QuestionCount, so I know how many questions to extract 
    qnum += 1
    print questionid[qnum -1] + " " + qanswerkey[qnum -1]

#import re
#re.findall(r'\AT[1-9][A-Z][0-9][0-9]',file[22])
