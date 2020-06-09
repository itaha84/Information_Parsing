import csv
import constants
import parse_utilities
from datetime import datetime
from collections import defaultdict
import itertools

# for name in constants.file_names:
#     with open(name)as f:
#         print(name)
#         print(next(f))
#         print(next(f))
#         print(next(f))
#     print()


# Examine the files
# for name in constants.file_names:
#     with open(name)as f:
#         print(name)
#         reader = csv.reader(f, delimiter=",", quotechar='"')
#         print(next(reader))
#         print(next(reader))
#     print("\n\n")

# including header rows
# for fname in constants.file_names:
#     print(fname)
#     reader = parse_utilities.csv_parser(fname, header=True)
#     print(next(reader))
#     print(next(reader))
#     print()

# Yielding excluding the headers
# for fname in constants.file_names:
#     print(fname)
#     reader = parse_utilities.csv_parser(fname, header=False)
#     print(next(reader))
#     print(next(reader))
#     print()


# # testing the date parser
# print(parse_utilities.parse_date('2017-10-07T00:14:42Z'))


# Testing the header extract function
# for filename in constants.file_names:
#     print(filename)
#     print(parse_utilities.extract_field_names(filename), end="\n\n")


# Testing iter file
# for fname, parser, nt_class in zip(constants.file_names, constants.parser_functions, constants.nt_names):
#     file_iter = parse_utilities.iter_file(fname, parser, nt_class)
#     print(fname)
#     for _ in range(5):
#         print(next(file_iter))
#     print("\n\n")


# gen = parse_utilities.combo_nt_gen(constants.file_names,
#                                    constants.parser_functions, constants.nt_names, constants.compress_list)
# # print(parse_utilities.combo_nt_header_gen(constants.file_names, constants.compress_list))
# # for i in range(5):
# # 	print(next(gen))
# #
# # # print("_______________________________________")

# cutoff_date = datetime(2017, 3, 1)


# def group_key(row):
#     return row.gender, row.vehicle_make


# data = parse_utilities.combo_nt_gen_filtered(constants.file_names, constants.parser_functions,
#                                              constants.nt_names,  constants.compress_list,
#                                              filter_key=lambda data: data.last_updated >= cutoff_date)

# sorted_data = sorted(data, key=group_key)
#
# grouped_data_f = itertools.groupby(sorted_data, key=group_key)
# grouped_data_m = itertools.groupby(sorted_data, key=group_key)
#
# group_f = (row for row in grouped_data_f if row[0][0] == "Female")
# group_m = (row for row in grouped_data_m if row[0][0] == "Male")
#
# result_f = ((row[0][1], len(list(row[1]))) for row in group_f)
# result_m = ((row[0][1], len(list(row[1]))) for row in group_m)
#
# for i in result_f:
#     print(i)

# for row in group_f:
#     print(row)
#
# print("**************")
#
# for row in group_m:
#     print(row)


data = parse_utilities.combo_nt_gen_filtered(constants.file_names, constants.parser_functions,
                                             constants.nt_names,  constants.compress_list,
                                             filter_key=lambda row: row.gender == "Male",
                                             sort_key= lambda row: row.vehicle_make )

for row in data:
    print(list(row))