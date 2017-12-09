from sys import argv

script, username = argv
prompt = '>'

print "Hi %s, I'm the %s script." % (username, script)
print "I'd like to ask you  few questions."
print "Do you like me %s?" % username
likes = raw_input(prompt)

print "Where Do you live %s?" % username
lives = raw_input(prompt)

print "what kind of computer do you have?  " 
computer = raw_input(prompt)


print """
Allright, so you said %r about liking me.
you live in %r. Not sure where that is.
And you have a %r computer. Nice.
""" % (likes, lives, computer)

