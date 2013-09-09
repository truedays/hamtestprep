#!/usr/bin/python2.7
#
# this will be a complete rewrite of hamtestprep in pythion 2.x

import re
f = open('dos2unix.out', 'r')
file = f.readlines()
questionid = ["",]
answerkey= ["",]
qnum = 0

for n in range(0,100):
#for n in range(0,2816):
  if file[n] == "~~\n":
    questionid[qnum:] = [file[n-6][0:5]]
    #answerkey[qnum:] = [re.sub(r'.*\(|\).*','',file[n-6],0)]
    answerkey[qnum:] = file[n-6][file[n-6].find("(")+1]
    #re.sub(r'.*\(|\).*','',[file[n-5]])
    if questionid[qnum] == '\n':
        questionid[qnum:] = [file[n-5][0:5]]
        #answerkey[qnum:] = [re.sub(r'.*\(|\).*','',file[n-5])]
        answerkey[qnum:] = file[n-5][file[n-5].find("(")+1]
# TODO: add QuestionCount, so I know how many questions to extract 
    qnum += 1
    print questionid[qnum -1]
    print questionid[qnum -1:]
    print answerkey[qnum -1]
print questionid[6]
print questionid
questionid[len(questionid):] = ["thisworks"]
print questionid
#import re
#re.findall(r'\AT[1-9][A-Z][0-9][0-9]',file[22])
