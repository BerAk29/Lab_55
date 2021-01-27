from os import strerror

try:
    cnt = 0
    s = open('text.txt', "rt")
    ch = s.read(1)  # will read the first char
    while ch != '':
        print(ch, end='')
        cnt += 1
        ch = s.read(1)  # will read the next char
    s.close()
    print("\nCharacters in file:", cnt, "\n")
except IOError as e:
    print("I/O error occurred: ", strerror(e.errno))


''' If you're absolutely sure that the file's length is safe and you can read the whole file to the memory at once, 
you can do it - the read() function, invoked without any arguments or with an argument that evaluates to None, 
will do the job for you.'''
try:
    cnt = 0
    s = open('text.txt', "rt")
    content = s.read()  # this will read the whole file (memory issue can happened)
    for ch in content:
        print(ch, end='')
        cnt += 1
    s.close()
    print("\nCharacters in file:", cnt)
except IOError as e:
    print("I/O error occurred: ", strerr(e.errno))


'''If you want to treat the file's contents as a set of lines, not a bunch of characters, 
the readline() method will help you with that. The method tries to read a complete line of text from the file, 
and returns it as a string in the case of success. Otherwise, it returns an empty string.
This opens up new opportunities - now you can also count lines easily, not only characters.'''
try:
    ccnt = lcnt = 0
    s = open('text.txt', 'rt')
    line = s.readline()
    while line != '':
        lcnt += 1
        for ch in line:
            print(ch, end='')
            ccnt += 1
        line = s.readline()
    s.close()
    print("\n\nCharacters in file:", ccnt)
    print("Lines in file:     ", lcnt)
except IOError as e:
    print("I/O error occurred:", strerror(e.errno))


'''The readlines() method, when invoked without arguments, 
tries to read all the file contents, and returns a list of strings, one element per file line.'''
try:
    ccnt = lcnt = 0
    s = open('text.txt', 'rt')
    lines = s.readlines(20)
    while len(lines) != 0:
        for line in lines:
            lcnt += 1
            for ch in line:
                print(ch, end='')
                ccnt += 1
        lines = s.readlines(10)
    s.close()
    print("\n\nCharacters in file:", ccnt)
    print("Lines in file:     ", lcnt)
except IOError as e:
    print("I/O error occurred:", strerror(e.errno))



'''Writing text files seems to be simpler, as in fact there is 
one method that can be used to perform such a task.'''
try:
	fo = open('newtext.txt', 'wt') # A new file (newtext.txt) is created.
	for i in range(10):
		s = "line #" + str(i+1) + "\n"
		for ch in s:
			fo.write(ch)
	fo.close()
except IOError as e:
	print("I/O error occurred: ", strerror(e.errno))



