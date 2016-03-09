""" A program that stores and updates a counter using a Python pickle file"""

import os.path 
import sys
import pickle 

def update_counter(filename, reset=False):
	""" Updates a counter stored in the file 'file_name'

		A new counter will be created and initialized to 1 if none exists or if
		the reset flag is True.

		If the counter already exists and reset is False, the counter's value will
		be incremented.

		file_name: the file that stores the counter to be incremented.  If the file
				   doesn't exist, a counter is created and initialized to 1.
		reset: True if the counter in the file should be rest.
		returns: the new counter value

	>>> update_counter('blah.txt',True)
	1
	>>> update_counter('blah.txt')
	2
	>>> update_counter('blah2.txt',True)
	1
	>>> update_counter('blah.txt')
	3
	>>> update_counter('blah2.txt')
	2
    >>> update_counter('blah.txt', True)
    1
	"""
        # Checks if file already exists and if the file doesn't need to be reset
        if os.path.exists(filename) == True and reset == False: 
            f = open(filename, 'r+') # opens the text file
            counter = pickle.load(f) # loads the text file as a pickle file
            counter += 1 # adds 1 to the counter
            f.seek(0,0)
            pickle.dump(counter, f) # adds the new counter back to the file
            f.close() # closes the file

        # if the file doesn't already exist or if it needs to be reset
        else: 
            new_file = open(filename, 'w') # creates a new file
            pickle.dump(1, new_file) # adds the first counter to it
            new_file.close() # closes the file

        file1 = pickle.load(open(filename, 'r')) 
        return file1 

if __name__ == '__main__':
	if len(sys.argv) < 2:
		import doctest
		doctest.testmod()
	else:
		print "new value is " + str(update_counter(sys.argv[1]))
        