###############################
#           Env               #

import sys
import numpy as np
import pandas as pd
import json
import re

#import configuration script
import config

#import vcf module
sys.path.append('/Users/caryn/Dropbox/Project_RiceGeneticVariation/database')
import vcf

#to time the program:
import time

###############################
#          Methods            #

def get_vcf_reader():
	return vcf.Reader(open(config.VCF, 'r'))

def parse_input( gene_str ):
	g_split = gene_str.split('g')[0]
	chrom_split = g_split.split('Os')[1]
	return chrom_split

def get_MSU_info ( gene ):
	chromNumber = parse_input(gene)
	#print chromNumber
	infoFile = config.CHROM_INFO_PATH[chromNumber]
	info = open(infoFile, 'r')
	gene_info = []
	myregex = r".*\s" + re.escape(gene) + r"\s.*"
	for line in info:
		if re.match(myregex, line):
			gene_info.append(line)
	#error message for not found:
	if (len(gene_info) == 0):
		error = "Gene not found."
		return error
	
	#check for multiple isoform information
	#print len(gene_info)
	if (len(gene_info) > 1):
		maxlen = 0
		gene_info_keep = []
		#get the lengths of all the gene isoforms
		for line in gene_info:
			splitline = line.split('\t')
			length = int(splitline[4]) - int(splitline[3])
			if (length > maxlen):
				maxlen = length
				gene_info_keep = [line]
		return gene_info_keep
	
	#if there are no isoforms, return gene_info
	return gene_info

def write_vcf(msu_info):
	msu = msu_info[0].split('\t')
	chrom = msu[0]
	start = int(msu[3])
	end = int(msu[4])

	vcf_reader = get_vcf_reader()
	vcf_writer = vcf.Writer(open('/Users/caryn/Dropbox/Project_jsLearn/simple_genes/public/python/tmp/region.vcf', 'w'), vcf_reader)

	for rec in vcf_reader.fetch(chrom, start, end):
		vcf_writer.write_record(rec)
		print rec

###############################
#            Main             #

if __name__ == '__main__':
	file, gene = sys.argv

	msu_info = get_MSU_info(gene)
	write_vcf(msu_info)
	sys.stdout.flush()


