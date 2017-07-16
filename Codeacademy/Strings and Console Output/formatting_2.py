name = raw_input("What is your name?")
quest = raw_input("What is your quest?")
color = raw_input("What is your favorite color?")

''' The / is required... otherwise the interpreter doesnt know its suppose to
consider the line break as a string continuation '''

print "Ah, so your name is %s, your quest is %s, " \
"and your favorite color is %s." % (name, quest, color)
