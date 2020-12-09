# there is a CSV library
import csv

def MergeCSV(infiles, out):
    headers = dict()
    hdr = dict()
    mycsv = list()

    # iterate the files
    for f in infiles:
        fhand = open(f)
        lineN  = 0
        # iterate the lines
        for line in fhand:
            hi = 0
            # the first line is the header
            if lineN == 0:
                lineN += 1
                # split the line to get the headers
                for h in line.rstrip().split(','):
                    # save the headers 
                    if h in headers.keys():
                        headers[h] = max(hi, headers[h])
                    else:
                        headers[h] = hi
                    # save the header as an index in the dictionary
                    hdr[hi] = h
                    # increment that index    
                    hi += 1
            # other lines are data
            else:
                rec = dict()
                # split the line to get the data
                for i in line.rstrip().split(','):                    
                    rec[hdr[hi]] = i
                    hi += 1
                # save the record
                mycsv.append(rec)
    
    # debug data
    #print(headers)
    #print(hdr)
    #print(mycsv)

    # put the headers in order
    hList = [0] * len(headers.keys())
    for k in headers: hList[headers[k]] = k
    #print(hList)
    
    # write headers to the file
    file = open(out, 'w')
    file.write((',').join(hList))
    print((',').join(hList))
    
    # update the existing records
    for r in mycsv:
        rec = list()
        for i in hList:
            if not i in r: rec.append('')
            else: rec.append(r[i])
        file.write((',').join(rec))
        print((',').join(rec))
        
    file.close()    

MergeCSV(['class2.csv', 'class1.csv'], 'classes.csv')

def merge_csv(csv_list, output_path):
    # build list with field names
    fields = list()
    for file in csv_list:
        with open(file, 'r') as input_csv:
            # csv dict reader
            fn = csv.DictReader(input_csv).fieldnames
            # extend on new field names
            fields.extend(x for x in fn if x not in fields)

    # write data out
    with open(output_path, 'w', newline='') as output_csv:
        writer = csv.DictWriter(output_csv, fieldnames=fields)
        writer.writeheader()
        for file in csv_list:
            with open(file, 'r') as input_csv:
                reader = csv.DictReader(input_csv)
                for row in reader:
                    writer.writerow(row)

merge_csv(['class1.csv', 'class2.csv'], 'all_classes.csv')
