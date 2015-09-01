name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
weight = 180 #lbs
eyes = 'Blue'
teeth = 'white'
hair = 'Brown'
centimeter_height = height * 2.54
kilogram_weight = weight / 2.2

print "let's talk about %s." % name
print "He's %d inches tall." % height
print "He's %f centimeters tall." % centimeter_height
print "He's %d pounds heavy." % weight
print "he's %f kilograms heavy." % kilogram_weight
print "Actually that's not to heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (age, height, weight, age + height + weight)
