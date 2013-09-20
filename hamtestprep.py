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

##print "len:", + len(argv)
#if len(argv) != 2:
#  print "Expected a numeric value. Try running:",
#  print argv[0],
#  print "2"
#  exit(1)

f = open('Revised Element 2.txt', 'r')
file = f.readlines()
question = []
qnum = 0
correctans = 0

#for n in range(0,2816):
for n in range(0,len(file)):
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

# section questioncounter
sectn = 0
section = {'T1A':[], 'T1B':[], 'T1C':[], 'T1D':[], 'T1E':[], 'T1F':[], 'T2A':[], 'T2B':[], 'T2C':[], 'T2D':[], 'T2E':[], 'T2F':[], 'T3A':[], 'T3B':[], 'T3C':[], 'T3D':[], 'T3E':[], 'T3F':[], 'T4A':[], 'T4B':[], 'T4C':[], 'T4D':[], 'T4E':[], 'T4F':[], 'T5A':[], 'T5B':[], 'T5C':[], 'T5D':[], 'T5E':[], 'T5F':[], 'T6A':[], 'T6B':[], 'T6C':[], 'T6D':[], 'T6E':[], 'T6F':[], 'T7A':[], 'T7B':[], 'T7C':[], 'T7D':[], 'T7E':[], 'T7F':[], 'T8A':[], 'T8B':[], 'T8C':[], 'T8D':[], 'T8E':[], 'T8F':[], 'T9A':[], 'T9B':[], 'T9C':[], 'T9D':[], 'T9E':[], 'T9F':[], 'T0A':[], 'T0B':[], 'T0C':[], 'T0D':[], 'T0E':[], 'T0F':[]}
for x in range(0, qnum):
  if question[x][0][0:3] == "Del": # Skip if Deleted
    continue
  section[question[x][0][0:3]].append(x)

# main exam loop. Randomize section-questions to mimic a real exam
qcount = 0
for x in sorted(section.keys()):
  if section[x] == []:
   # print "Empty set. Skipping..."
    continue
  Q = section[x][randint(0,len(section[x])-1)]
  #print x
  #print "L ==== " +str(len(section[x])-1)
  #print "Q ==== " + str(Q)
  #print x
  #print section[x]
  #print question[Q]
  while "igure" in question[Q][2]:
    print "Skipping schematic based question",
    print question[Q][0]
    Q = section[x][randint(0,len(section[x])-1)]
  qcount += 1
  print "  " + question[Q][0] + "  " + str(qcount) + "/35"
  print "  " + question[Q][2],
  for n in question[Q][3]:
    print n,
  guess = ''
  while len(guess) != 1:
    while (guess != 'A') and (guess != 'B') and (guess != 'C') and (guess != 'D') and (guess != 'X'):
      guess = raw_input("Answer? ").upper()
#      guess = 'A'
    if guess == "X":
      guess = input("debug: ")
      print guess
    #  print question[Q][1]
    if guess == question[Q][1]:
      print "Correct!"
      print
      correctans += 1
      sleep(.5)
      continue
    else:
      print "Wrong!"
    #for n in "ABCD"  This loop looks for the right answer to display after user gets it wrong
    for n in range(0,4):
      #print question[Q][1]+". " + " " + question [Q][3][n]
      if question[Q][1]+". " in question[Q][3][n]:
        print question[Q][3][n]
        break
    sleep(1)
#final = round(float(correctans)/float(35,2))
final = round(float(correctans)/35,2)
print
print "you scored: {0:.2f}%".format(final*100)
print "You had %d out of %d correct" % (correctans, 35)
if correctans >= 26:
  print "You Passed!!!"
else:
  print "Sorry, you needed to get at least 26 questions correct to be considered passing"
print
##old fully random question loop
#for x in range(int(argv[1])):
##  print x
##  print argv[1]
#  Q = randint(0,qnum)
#  while "igure" in question[Q][2]:
#    print "Skipping schematic based question",
#    print question[Q][0]
#    Q = randint(0,qnum)
#  print
#  print "  " + "#"+str(x+1) + " of " + argv[1] + "  [" + question[Q][0] + "]\t\t++debug++"
#  print "  " + question[Q][2],
#  for n in question[Q][3]:
#    print n,
#  guess = ''
#  while len(guess) != 1:
#    while (guess != 'A') and (guess != 'B') and (guess != 'C') and (guess != 'D') and (guess != 'X'):
#      guess = raw_input("Answer? ").upper()
#  if guess == "X":
#    guess = input("debug: ")
#    print guess
##  print question[Q][1]
#  if guess == question[Q][1]:
#    print "Correct!"
#    correctans += 1
#    sleep(.5)
#    continue
#  else:
#    print "Wrong!"
#    #for n in "ABCD"
#    for n in range(0,4):
#      #print question[Q][1]+". " + " " + question [Q][3][n]
#      if question[Q][1]+". " in question[Q][3][n]:
#        print question[Q][3][n]
#        break
#    sleep(1)
#
#final = round(float(correctans)/float(argv[1]),2)
#print
#print "you scored: {0:.2f}%".format(final*100)
#print "You had %d out of %d correct" % (correctans, int(argv[1]))
#print
