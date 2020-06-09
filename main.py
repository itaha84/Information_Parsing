import constants
import parse_utilities


data = parse_utilities.combo_nt_gen_filtered(constants.file_names, constants.parser_functions,
                                             constants.nt_names,  constants.compress_list,
                                             filter_key=lambda row: row.gender == "Male",
                                             sort_key= lambda row: row.vehicle_make )

for row in data:
    print(row)