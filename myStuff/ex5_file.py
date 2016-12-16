from sys import argv
script, filename = argv
txt = open(filename, "a+")
print "here is your file %r :" % filename
print txt.read()
txt.close()
txt = open(filename, "a+")
txt.write("new lines added\n")
txt.close()
print ("filename again please")
file_again = raw_input("> ")
txt_again = open( file_again)
print txt_again.read()
txt_again.close()
