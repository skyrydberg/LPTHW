# Exercise 3: Numbers and Math
# I addressed Exercises 1 & 2 in the same post because they
# are trivial. This one gets its own post.

print "I will now count my chickens:"

# Note the order of operations holds here, a kind programmer
# would type this 25 + (30 / 6) for clarity, we divide 30 by 6
# and then add the result to 25
print "Hens", 25 + 30 / 6

# Similarly 100 - ((25 * 3) % 4), we multiply 25 by 3 and then
# divide by 4 and take the remainder, which we then subtract
# from 100
print "Roosters", 100 - 25 * 3 % 4

print "Now I will count the eggs:"

# And again 3 + 2 + 1 - 5 + (4 % 2) - (1 / 4) + 6 or more
# realistically you'd split this across a couple lines...
# Regardless, we divide 1 by 4 and divide 4 by 2 and keep the
# remainder then we sum across. Note per Study Drill 3 I've
# replaced 1 with 1.0 to force python to evaluate the values
# as floating point numbers instead of integers
print 3 + 2 + 1 - 5 + 4 % 2 - 1.0 / 4 + 6

print "Is it true that 3 + 2 < 5 - 7?"

print 3 + 2 < 5 - 7

print "What is 3 + 2?", 3 + 2
print "What is 5 - 7?", 5 - 7

print "Oh that's why it's False."

print "How about some more."

print "Is it greater?", 5 > -2
print "Is it greater or equal?", 5 >= -2
print "Is it less or equal?", 5 <= -2
