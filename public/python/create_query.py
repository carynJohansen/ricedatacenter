###############################
#           Env               #

import sys
from BCBio import GFF
from sqlalchemy import create_engine
from pandas.io import sql
import pandas as pd
import numpy as np
import json
import ast

import config

#to time the program:
import time

###############################
#          Methods            #

def if_all_genes ( inpt ):
	if (isinstance(inpt['geneSelectInput'], dict)):
		return 0
	else:
		return 1

def parse_input ( inpt ):
	query = []
	select = inpt['select']
	category = inpt['category']

	query.append("SELECT regulator_gene.gene_locus as regulator, net.regulator as netID_regulator,")
	query.append("target_gene.gene_locus as target, net.target as netID_target")
	query.append("FROM interaction_network as net")
	query.append("INNER JOIN gene_model as regulator_gene ON (net.regulator = regulator_gene.id)")
	query.append("INNER JOIN gene_model as target_gene ON (net.target = target_gene.id)")

	# if it is all genes
	if ( if_all_genes( inpt ) == 1 ):
		querySTR = "\n".join(query)

	# if there is a specific
	if ( if_all_genes( inpt ) == 0 ):
		gene = inpt['geneSelectInput']['gene']
		if (category == "regulator"):
			query.append("WHERE regulator_gene.gene_locus = '%s'" % gene)
		if (category == "target"):
			query.append("WHERE target_gene.gene_locus = '%s'" % gene)
		if ( category == "either"):
			query.append("WHERE regulator_gene.gene_locus = '%s' OR target_gene.gene_locus = '%s'" % (gene, gene))
		querySTR = "\n".join(query)
	
	return querySTR

###############################
#            Main             #

if __name__ == '__main__':
	#file, j = sys.argv
	injson = ast.literal_eval(sys.argv[1])

	x = parse_input(injson)

	#print if_all_genes(injson)
	print x
	sys.stdout.flush()
