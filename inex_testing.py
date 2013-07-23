# Oh God, here we go.  I have no idea if any of this crap actually works,
# as I can only write (not test) until I get home from work.  Also, I
# know jack about what I'm doing, so it's a ton of trial and error.

# The purpose of this script is to attempt opening
# a file and locating a specific string from a second file
# within the first file.  Should be a simple 'open this file'
# and then 'check for this file's txt within the first file'.

vector = raw_input("Enter vector sequence file: ") # The large file of the vector
filenamev = raw_input()
f = open('filenamev', 'r')
print f # only printing right now to test if this is working

sequence = raw_input("Enter sequencing result file: ") # The short(er) result file
filenames = raw_input()
f = open('filenames', 'r')
print f # only printing right now to test if this is working



# The kicker is that what I really need to be able to find is
# a string that BEGINS with characters in the vector file but
# eventually switches to unknown sequence.  That unknown sequence
# is what I would like to RETURN to the user.



# loop?  Take the sequence file and look at the first letter
# and search for that letter in the vector file, then loop around
# and search for the first two letters in the vector file, then
# the first three letters.  This will start the program locating
# the vector sequence that starts every sequence file.  Continue
# looping, and when the loop finally reaches the character that does
# not match the vector sequence, have it copy the remainder of the
# sequence file (the insert, now that the vector sequence has been
# removed) to a new .txt file.  Figure out input/output later.

# loop break could happen by requesting how many copies of the
# looping sequence are found.  Once the loop hits "1" copy found
# you must continue to loop to account for base pairs that are
# only found in that instance but are still part of the vector.
# only once the loop returns "0" matches do you know that you
# found the end of the vector and can RETURN the rest of the data.
