x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." %(binary,do_not)

print x
print y

print "I said : %r." %x     #1
print "I also said: '%s'. " %y   #2

hilarious = False
joke_evaluation = "Isn't that jole so funny?! %r"   #4
  
print joke_evaluation % hilarious    #3

w = "This is  the left side of..."
e = "a string with a right side."

print w + e