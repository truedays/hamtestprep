#!/usr/bin/python3
#
# Ham Test Prep
# Ray @ truedays.org
# https://github.com/truedays/hamtestprep
# http://truedays.org/hamtestprep
#

# Check if file exist
# todo
import re
#qregexp = re.compile(r"T1A01 (D) [97.3(a)(4)]")
##qregexp = re.compile(r"T[0-9][A-F][0-9][0-9]\ ?.*)
# Open test pool file as f
f = open("dos2unix.out", 'r')
qnum = 0
questionid = ["", "", ""]
answer = ["", "", "", ""]
questions = ["","","",""]
#
#while f.readline() not "~ End of Syllabus"
#print("ray")
#f.readline()

#for line in f:
#	print(line, end='')
	
# put file in list variable
file = f.readlines()
for n in range(0,7000):
#    x = file[n].split("(",1)
#    print(x)a
    if file[n] == "~~\n":
        #print(file[n-6][0:6])
        
        questionid[qnum] = [file[n-6][0:5]]
        answer[qnum] = [file[n-6][7:8]]
        questions[qnum] = file[n-5] + file[n-4] + file[n-3] + file[n-2] + file[n-1] 
        qnum = qnum + 1
##   Question ID/line number  | Question | Answer
#if n == "~~" then:"
    print(n,end=' ')
    print(file[n],end='')

#print ("question id is {0}".format(question[0]))
print ("_____________________________")
print (questionid[0])
print (answer[0])
if questionid[0] == ['T1A01']:
	print ("it doesn't care about the stupid square bracketrs")
print (questions[0])