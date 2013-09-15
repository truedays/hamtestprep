#!/usr/bin/python2.7
#
# Ham(radio)TestPrep 
# Ray at truedays.org
# https://github.com/truedays/hamtestprep
# 
# todo: http/cgi, generate real tests with proper number of questions per 
#  section, prevent repeat "known" questions from cram mode. add multi-test 
#  modes: 1) exam 2) cramsession 3) section cram. toggle display answer after 
#  incorrect guesses

from random import randint
from sys import argv, exit
from time import sleep

#print "len:", + len(argv)
if len(argv) != 2:
  print "Expected a numeric value. Try running:",
  print argv[0],
  print "2"
  exit(1)

f = open('dos2unix.out', 'r')
file = f.readlines()
question = []
qnum = 0
correctans = 0

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
#  print x
#  print argv[1]
  Q = randint(0,qnum)
  while "igure" in question[Q][2]:
    print "Skipping schematic based question",
    print question[Q][0]
    Q = randint(0,qnum)
  print
  print question[Q][2],
  for n in question[Q][3]:
    print n,
  guess = raw_input("Answer? ")
  #print guess.upper()
#  print question[Q][1]
  if guess[0].upper() == question[Q][1]:
    print "Correct!"
    correctans += 1
    sleep(.5)
    continue
  else: 
    print "Wrong!"
    sleep(1)

final = round(float(correctans)/float(argv[1]),2)
print
print "you scored: {0:.2f}%".format(final*100)
print "You had %d out of %d correct" % (correctans, int(argv[1]))
print 
#if final == 1.0:
#  print "You got 100%!"
#else:
#  print "You scored: ", final
