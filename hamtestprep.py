#!/usr/bin/python2.7
#
# this will be a complete rewrite of hamtestprep in pythion 2.x

from random import randint
from sys import argv, exit

print "len:", + len(argv)
if len(argv) != 2:
  print "Expected a numeric value. Try running:",
  print argv[0],
  print "2"
  exit(1)

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



for x in range(int(argv[1])):
  print x
  print argv[1]
  Q = randint(0,qnum)
  print question[Q][2],
  for n in question[Q][3]:
    print n,
  guess = raw_input("Answer? ")
  print guess.upper()
  print question[Q][1]
  if guess.upper() == question[Q][1]:
    print "Correct!" 
    continue
  else: 
    print "Wrong!"
