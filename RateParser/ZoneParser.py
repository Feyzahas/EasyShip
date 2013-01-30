import argparse, re

import Utils


def open_file(path):
    return open(path, 'r')


def print_results_as_yaml(results,arguments):
    for (counter, rate) in enumerate(results):
        print "- model: root.rate"
        print "  pk: " + str(arguments.pk + counter)
        print "  fields:"
        print "    weight: " + rate['weight']
        print "    service_level: " + str(arguments.service)
        print "    zone_number: " + rate['zone']
        print "    price: " + rate['rate']

def parse_file(arguments):
    file = open_file(file)
    parse_lines(file)



def parse_lines(file):
	for line in file:
		line_values=line.split(',')
		first_value,second_value=line_values[0].split('-')
		for x in range(int(first_value),int(second_value)+1)
			print x		
  		
	

