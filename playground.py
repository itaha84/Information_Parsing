import csv
import constants
import parse_utilities
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


# Testing combo_nt_header_gen to generate combo NT fields
# print(parse_utilities.combo_nt_header_gen(constants.file_names, constants.compress_list))

# Testing chaining iter_file to generate 4 chained NamedTuples
# y = (list(itertools.chain(zip(parse_utilities.iter_file(constants.personal_file, constants.personal_parser,constants.personal_nt),
#                                                                    parse_utilities.iter_file(constants.vehicles_file, constants.vehicle_parser,constants.vehicle_nt),
#                                                                    parse_utilities.iter_file(constants.employment_file, constants.employment_parser,constants.employment_nt),
#                                                                    parse_utilities.iter_file(constants.updated_status, constants.status_parser,constants.status_nt)))))
# print(list(itertools.chain.from_iterable(y[0])))
# print(list(itertools.compress(itertools.chain.from_iterable(y[0]), constants.compress_list)))


# y = (itertools.chain(zip(parse_utilities.iter_file(constants.personal_file, constants.personal_parser,constants.personal_nt),
#                                                                    parse_utilities.iter_file(constants.vehicles_file, constants.vehicle_parser,constants.vehicle_nt),
#                                                                    parse_utilities.iter_file(constants.employment_file, constants.employment_parser,constants.employment_nt),
#                                                                    parse_utilities.iter_file(constants.updated_status, constants.status_parser,constants.status_nt))))
# print(next(y))

gen = parse_utilities.combo_nt_gen(constants.file_names, constants.parser_functions, constants.nt_names, constants.compress_list)
# print(parse_utilities.combo_nt_header_gen(constants.file_names, constants.compress_list))
for i in range(5):
	print(next(gen))

