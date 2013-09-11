#!/usr/bin/python2.7
#
# this will be a complete rewrite of hamtestprep in pythion 2.x

f = open('dos2unix.out', 'r')
file = f.readlines()
question = []
qnum = 0

for n in range(0,2816):
  if file[n] == "~~\n":
    if file[n-6][0:5] == '\n':
      question.append([file[n-5][0:5]])
      question[qnum].append(file[n-5][7:8])
      question[qnum].append(file[n-4])
      question[qnum].append([file[n-3], file[n-2], file[n-1]])
    else:
      question.append([file[n-6][0:5]])
      question[qnum].append(file[n-6][7:8])
      question[qnum].append(file[n-5])
      question[qnum].append([file[n-4], file[n-3], file[n-2], file[n-1]])
    #print question[qnum]
    qnum += 1

# for Q in range(qnum)
print question[0][2],
for n in question[0][3]:
  print n,
