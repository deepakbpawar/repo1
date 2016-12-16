from subprocess import call
from sys import argv
script,filename,word1,word2 = argv
file1=open(filename,"a+")
filename2 = "newfile.txt"
print "replacing %s with %s", word1, word2
file2=open(filename2, "w")
#while (line= file1.readline()):
#line= file1.readline()
for line in file1:
    line2=line.replace(word1,word2)
    file2.write(line2)
file1.close()
file2.close()
print "file1 contents are"
call("type " + filename , shell=True)
print "\n"
call("type " + filename2, shell=True)
file1.close()
file2.close()
