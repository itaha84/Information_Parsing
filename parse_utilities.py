import csv
import itertools
from datetime import datetime
from collections import namedtuple


def csv_parser(fname, *, delimiter=",", quotechar='"', header=False):
	with open(fname)as f:
		reader = csv.reader(f, delimiter=delimiter, quotechar=quotechar)
		if not header:
			next(f)
		yield from reader


def parse_date(value, *, fmt="%Y-%m-%dT%H:%M:%SZ"):
	return datetime.strptime(value, fmt)


def extract_field_names(fname):
	with open(fname)as f:
		reader = csv.reader(f, delimiter=",", quotechar='"')
		return next(reader)


def creating_named_tuple(nt_name, fname):
	fields = extract_field_names(fname)
	return namedtuple(nt_name, fields)


def iter_file(fname, parser, nt_name):
	nt_class = creating_named_tuple(nt_name, fname)
	reader = csv_parser(fname)
	for row in reader:
		parsed_data = (parser_fn(value) for parser_fn, value in zip(parser, row))
		yield nt_class(*parsed_data)


def combo_nt_header_gen(files, selector):
	combo_nt_fields = []
	for file in files:
		combo_nt_fields.append(extract_field_names(file))
	combo_nt_fields_chained = list(itertools.chain.from_iterable(combo_nt_fields))
	combo_nt_fields_cleaned = list(itertools.compress(combo_nt_fields_chained, selector))
	return combo_nt_fields_cleaned


def combo_nt_gen(files, parsers, nt_names, sel):
	zipped_tuples = zip(*(iter_file(file, parser, nt_name) for file, parser, nt_name in zip(files, parsers, nt_names)))
	merged_tuple = (itertools.chain.from_iterable(zipped_tuple) for zipped_tuple in zipped_tuples)
	Data = namedtuple("Data", combo_nt_header_gen(files, sel))
	for row in merged_tuple:
		compressed_row = itertools.compress(row, sel)
		yield Data(*compressed_row)


def combo_nt_gen_filtered(files, parsers, nt_names, sel, *, filter_key=None, sort_key=None):
	iter_combo = combo_nt_gen(files, parsers, nt_names, sel)
	iter_combo_filtered = filter(filter_key, iter_combo)
	if not sort_key:
		yield from iter_combo_filtered
	else:
		iter_combo_filtered_sorted = sorted(iter_combo_filtered, key=sort_key)
		iter_combo_filtered_sorted_grouped = itertools.groupby(iter_combo_filtered_sorted, key=sort_key)
		yield from ((row[0], len(list(row[1]))) for row in iter_combo_filtered_sorted_grouped)
		# yield from iter_combo_filtered_sorted_grouped



