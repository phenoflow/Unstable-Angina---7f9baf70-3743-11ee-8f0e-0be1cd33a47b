# Kuan V, Denaxas S, Gonzalez-Izquierdo A, Direk K, Bhatti O, Husain S, Sutaria S, Hingorani M, Nitsch D, Parisinos C, Lumbers T, Mathur R, Sofat R, Casas JP, Wong I, Hemingway H, Hingorani A, 2023.

import sys, csv, re

codes = [{"code":"G311.13","system":"readv2"},{"code":"G311100","system":"readv2"},{"code":"1431","system":"med"},{"code":"17307","system":"med"},{"code":"19655","system":"med"},{"code":"36523","system":"med"},{"code":"39449","system":"med"},{"code":"39655","system":"med"},{"code":"4656","system":"med"},{"code":"54251","system":"med"},{"code":"66388","system":"med"},{"code":"7347","system":"med"},{"code":"9276","system":"med"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('unstable-angina-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["angina---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["angina---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["angina---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
