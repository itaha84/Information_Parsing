import itertools
from parse_utilities import parse_date

# Files
personal_file = "data/personal_info.csv"
vehicles_file = "data/vehicles.csv"
employment_file = "data/employment.csv"
updated_status = "data/update_status.csv"
file_names = (personal_file, vehicles_file, employment_file, updated_status)

# Parsing functions
personal_parser = (str, str, str, str, str)
vehicle_parser = (str, str, str, int)
employment_parser = (str, str, str, str)
status_parser = (str, parse_date, parse_date)
parser_functions = (personal_parser, vehicle_parser, employment_parser, status_parser)


# Named Tuple class names for each file
personal_nt = "Personal"
vehicle_nt = "Vehicle"
employment_nt = "Employment"
status_nt = "Status"
nt_names = (personal_nt, vehicle_nt, employment_nt, status_nt)


# Creating a Truth Value for required fields for Goal 2 combo Tuple
personal_compress = [True, True, True, True, True]
vehicle_compress = [False, True, True, True]
employment_compress = [True, True, True, False]
status_compress = [False, True, True]
compress_all = (personal_compress, vehicle_compress,
                employment_compress, status_compress)
compress_list = list(itertools.chain.from_iterable(compress_all))

