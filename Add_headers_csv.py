import csv
import sys, threading
sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

#Code takes the fas_to_csv.py output and adds a "Group" Column, add headers for the 'Seq_ID', 'Seq' as well as it enumerates all possitons of the sequence.
#The output is in csv format and is ready to be used with the stdev_cal.py code.

dir = r'U:\ResearchData\rdss_hhaim\LAB PROJECTS\John\Galaxy Analysis\6.6.23 Troubleshooting\\'
filename_input = 'test.csv'  # Replace with your actual CSV file name
filename_output = 'test_mod_4.csv'

def add_headers_to_csv(input_filename, output_filename):
    with open(input_filename, 'r') as file:
        reader = csv.reader(file)
        data = list(reader)

    header = ['Group', 'Seq_ID', 'Seq']
    num_columns = len(data[0]) - len(header)
    header += [str(i) for i in range(1, num_columns + 2)]

    data.insert(0, header)

    for row in data[1:]:
        row.insert(0, '1')

    with open(output_filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)

input_filename = dir + filename_input
output_filename = dir + filename_output
add_headers_to_csv(input_filename, output_filename)
