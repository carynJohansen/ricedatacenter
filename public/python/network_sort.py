###############################
#           Env               #

import sys
from BCBio import GFF
from sqlalchemy import create_engine
from pandas.io import sql
import json
import re
import ast

#import config
#import vcf

#to time the program:
import time

###################
#    SQL Engine   #

engine = create_engine('sqlite:///' + config.DATABASE)
connect = engine.connect().connection

###############################
#          Methods            #

def get_vcf_reader():
	return vcf.Reader(open(config.VCF, 'r'))

def parse_input( gene_str ):
	g_split = gene_str.split('g')[0]
	chrom_split = g_split.split('Os')[1]
	return chrom_split

def create_sql_query ( input_str ):
	input_json = ast.literal_eval(input_str)
	#print input_json['select']

def sql_query():
	sql_st = '''SELECT gm1.gene_locus as reg,  \
					gm2.gene_locus as target \
					FROM interaction_network as net \
					INNER JOIN gene_model as gm1 ON (net.regulator = gm1.id) \
					INNER JOIN gene_model as gm2 ON (net.target = gm2.id) \
					WHERE net.regulator = 32039'''
	print sql_st
	data = sql.read_sql(sql_st, con=connect)
	print data

###############################
#            Main             #

if __name__ == '__main__':
	#file, json = sys.argv
	json = '{"select" : "all_genes","category" : "target", "snpeff" : ["START","INTRON","NSC"], "landrace" : ["japonica","tropical_japonica","indica","aus"]}'
	create_sql_query(json)
	sql_query()

	sys.stdout.flush()