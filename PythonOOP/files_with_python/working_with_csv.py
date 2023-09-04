import csv

with open("user_details.csv", newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    print(list(csvreader)[0][1])

    # skips first row with headings so able to iterate through data
    # iterable_csv = iter(csvreader)
    # next(iterable_csv)
    # for row in iterable_csv:
    #     print(row)

    # now data is contained in lists so can access values with indexing
    # print(csvreader)
    # for row in csvreader:
    #     print(row)
    #