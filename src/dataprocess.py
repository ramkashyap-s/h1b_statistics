import csv
from collections import defaultdict
import heapq
import argparse
import sys

def parse_input_arguments():
    """
    helper method to parse input arguments
    @return: args
    """
    print("--parsing input arguments")
    parser = argparse.ArgumentParser()

    parser.add_argument('-i', '--input_file', required=True,  default=None,
                        help='full path of the input file')

    parser.add_argument('-o1', '--output_file_occupations', required=True, default=None,
                        help='full path of the occupations output file')

    parser.add_argument('-o2', '--output_file_states', required=True, default=None,
                        help='full path of the states output file')

    parser.add_argument('-k', '--top_k', required=False, default=10, type=int,
                        help='return top k aggregated results; default = 10')

    parser.add_argument('-d', '--delimiter', required=False,  default=';',
                        help='delimiter for input and output files; default = semicolon')

    try:
        args = parser.parse_args()
        return args
    except:
        parser.print_help()
        exit(2)


def sort_key(x):
    """
    helper method for deciding the sorting order
    :param x:
    :return: list of keys by which sorting takes place
    """
    return -x[1], x[0]


def get_topk_metrics(args, occupation_column_name, state_column_name, status_column_name, status_value):
    """
    method that calculates top certified occupations and top certified states and returns top 10 results
    @:param args:
    @:param occupation_column_name:
    @:param state_column_name:
    @param state_column_name:
    """
    total_status_count = 0
    occupation_status_count = defaultdict(int)
    state_status_count = defaultdict(int)
    try:
        with open(args.input_file, newline='') as input_file:
            print('--reading input file and analyzing--')
            reader = csv.DictReader(input_file, delimiter=args.delimiter)
            for row in reader:
                # increment the certified count by one if the status value of entry is equal to the given status_value
                # e.g. if row is "Certified" then increment certified count
                if row[status_column_name].lower() == status_value.lower():
                    occupation_status_count[row[occupation_column_name]] += 1
                    state_status_count[row[state_column_name]] += 1
                    total_status_count += 1

        # find top k aggregate based on decreasing order of count and then alphabetically
        top_occupation_results = heapq.nsmallest(args.top_k, occupation_status_count.items(), key=sort_key)

        top_state_results = heapq.nsmallest(args.top_k, state_status_count.items(), key=sort_key)

        return top_occupation_results, top_state_results, total_status_count

    except Exception as error:
        print(sys.stderr, "Exception: %s" % str(error))
        sys.exit(1)


def output_data(args, output_file_path, top_k_results, total_status_count, output_columns):
    """
    helper method to write results to the files at the given output
    @param args:
    @param top_k_results:
    @param total_status_count:
    @:param output_columns:
    @:return none, write to the files at given output paths
    """

    try:
        with open(output_file_path, 'w', newline='') as output_file:
            print("--writing to output files--")
            writer = csv.DictWriter(output_file, fieldnames=output_columns, delimiter=args.delimiter)
            # write the header column first
            writer.writeheader()
            for key, count in top_k_results:
                writer.writerow({output_columns[0]: key,
                                 output_columns[1]: count,
                                 output_columns[2]: '{:.1%}'.format(count / total_status_count)})

    except Exception as error:
        print(error)
        exit(1)
