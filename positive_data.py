import csv

#determining the keyword probability from test statements
string = "The doctor was good . The appointment went well . The doctor was bad but his behaviour was good . The staff was nice ."

splitstring = string.split()

list = []

for word in splitstring:
    if word == 'doctor':
        list.append(word)

i = len(list) /string.count("." , 0 , len(string))

with open('pdataset.csv', 'w') as csvfile:
    filewriter = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    filewriter.writerow([list[0]])
    filewriter.writerow([i])

list.clear()

for word in splitstring:
    if word == 'appointment':
        list.append(word)

i = len(list) / string.count(".", 0, len(string))

with open('pdataset.csv', 'a+') as csvfile:
    filewriter = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    filewriter.writerow([list[0]])
    filewriter.writerow([i])

list.clear()

for word in splitstring:
    if word == 'bad':
        list.append(word)

i = len(list) / string.count(".", 0, len(string))

with open('pdataset.csv', 'a+') as csvfile:
    filewriter = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    filewriter.writerow([list[0]])
    filewriter.writerow([i])

list.clear()

for word in splitstring:
    if word == 'good':
        list.append(word)

i = len(list) / string.count(".", 0, len(string))

with open('pdataset.csv', 'a+') as csvfile:
    filewriter = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    filewriter.writerow([list[0]])
    filewriter.writerow([i])

list.clear()

for word in splitstring:
    if word == 'nice':
        list.append(word)

i = len(list) / string.count(".", 0, len(string))

with open('pdataset.csv', 'a+') as csvfile:
    filewriter = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    filewriter.writerow([list[0]])
    filewriter.writerow([i])

list.clear()

for word in splitstring:
    if word == 'staff':
        list.append(word)

i = len(list) / string.count(".", 0, len(string))

with open('pdataset.csv', 'a+') as csvfile:
    filewriter = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    filewriter.writerow([list[0]])
    filewriter.writerow([i])
