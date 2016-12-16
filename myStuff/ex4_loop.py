tabby_cat="\t I'm tabbed in"
persian_cat="I'm split \non a line"
backslash_cat="Im \\ a \\ cat"

fat_cat="""
I'll do a list
\t*Cat
\t*Fish
        *catnip
"""
fat_cat2='''
I'll do a list
    *Cat
    *Fish
    *catnip
'''
print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

print fat_cat2

print "================"
while True:
    for i in ["/","-","|","\\","|"]:
        print "%s\r" % i,
