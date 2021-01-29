''' This script show how to work with txt and file, date, time modules '''
''' Working on CSV File '''
import csv
#with open('datafile.csv','rt') as f:
#  data = csv.reader(f)
#  for row in data:
#       print(row)

''' Writing to CSV file input received '''

print("Please add a new router to the list")
hostname = input("What is the hostname? ")
ip = input("What is the ip address? ")
location = input("What is the location? ")
router = [hostname, ip, location]
with open("routerlist.csv", "a") as data:
    csv_writer = csv.writer(data)
    csv_writer.writerow(router)


''' Other CSV file, read CSV & print as a list '''
samplefile = open('routerlist.csv')
samplereader = csv.reader(samplefile)
sampledata = list(samplereader)

for item in sampledata:
    print(item)

print('\n')
print(sampledata)



"""
''' Dealing with text file'''
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


'''The OS Module, dealing with the Operating System patch, folder etc...'''
import os

os.makedirs("my_first_directory/my_second_directory")
os.chdir("my_first_directory")
print(os.getcwd())
os.chdir("my_second_directory")
print(os.getcwd())


os.mkdir("my_first_directory")
print(os.listdir())
os.rmdir("my_first_directory")
print(os.listdir())


''' Date and Time module'''
from datetime import date
from datetime import time
import time

today = date.today()

print("Today:", today)
print("Year:", today.year)
print("Month:", today.month)
print("Day:", today.day)


timestamp = time.time()
print("Timestamp:", timestamp)  # the value Timestamp: 1611786024.055511

d = date.fromtimestamp(timestamp)
print("Date:", d)  # the value Date: 2021-01-27

timestamp = 1572879180
print(time.ctime(timestamp))

d = date(1991, 2, 5)
print(d)  # 1991-02-05

d = d.replace(year=1992, month=1, day=16)
print(d)  # 1992-01-16




t = time(14, 53, 20, 1)
print("Time:", t)
print("Hour:", t.hour)
print("Minute:", t.minute)
print("Second:", t.second)
print("Microsecond:", t.microsecond)


''' to sleep or wait for a moment '''

class Student:
    def take_nap(self, seconds):
        print("I'm very tired. I have to take a nap. See you later.")
        time.sleep(seconds)
        print("I slept well! I feel great!")

student = Student()
student.take_nap(5)
"""