import csv

#determining the keyword probability from test statements
string = "The doctor was bad . The appointment was cancelled . The doctor was good  his behaviour was bad . The staff was rude ."

splitstring = string.split()

list = []

for word in splitstring:
    if word == 'doctor':
        list.append(word)

i = len(list) /string.count("." , 0 , len(string))

with open('ndataset.csv', 'w') as csvfile:
    filewriter = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    filewriter.writerow([list[0]])
    filewriter.writerow([i])

list.clear()

for word in splitstring:
    if word == 'appointment':
        list.append(word)

i = len(list) / string.count(".", 0, len(string))

with open('ndataset.csv', 'a+') as csvfile:
    filewriter = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    filewriter.writerow([list[0]])
    filewriter.writerow([i])

list.clear()

for word in splitstring:
    if word == 'bad':
        list.append(word)

i = len(list) / string.count(".", 0, len(string))

with open('ndataset.csv', 'a+') as csvfile:
    filewriter = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    filewriter.writerow([list[0]])
    filewriter.writerow([i])

list.clear()

for word in splitstring:
    if word == 'good':
        list.append(word)

i = len(list) / string.count(".", 0, len(string))

with open('ndataset.csv', 'a+') as csvfile:
    filewriter = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    filewriter.writerow([list[0]])
    filewriter.writerow([i])

list.clear()

for word in splitstring:
    if word == 'cancelled':
        list.append(word)

i = len(list) / string.count(".", 0, len(string))

with open('ndataset.csv', 'a+') as csvfile:
    filewriter = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    filewriter.writerow([list[0]])
    filewriter.writerow([i])

list.clear()

for word in splitstring:
    if word == 'rude':
        list.append(word)

i = len(list) / string.count(".", 0, len(string))

with open('ndataset.csv', 'a+') as csvfile:
    filewriter = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    filewriter.writerow([list[0]])
    filewriter.writerow([i])