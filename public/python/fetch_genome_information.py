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
#LOC_Os02g01110
def parse_input( gene_str ):
	g_split = gene_str.split('g')[0]
	chrom_split = g_split.split('Os')[1]
	return chrom_split

def get_vcf_reader():
	return vcf.Reader(open(config.VCF, 'r'))

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

def get_start_stop ( info_line ):
#	if (type(info_line) == )
	splitline = info_line[0].split('\t')
	info = {
		"chrom" : splitline[0],
		"gene_id" : splitline[1],
		"start" : int(splitline[3]),
		"end" : int(splitline[4]),
		"annotation" : splitline[9]
	}
	return info

def get_gene_gff (gene):
	chromNumber = parse_input(gene)
	infoFile = config.GFF_PATH[chromNumber]
	gff = open(infoFile, 'r')

	myregex = r".*" + re.escape(gene) + r".*"
	gene_gff = []
	for line in gff:
		if re.match(myregex, line):
			gene_gff.append(line)
	#print len(gene_gff)
	return gene_gff

def get_gene_gff_info (gene_gff, position):
	pos_gff_info = []

	prev_end = 0
	for line in gene_gff:
		splitline = line.split('\t')
		if position > int(splitline[3]) and position < int(splitline[4]):
			info_split = splitline[8].split(';')[0]
			iso_info = info_split.split(':')[0].split('=')[1]
			iso = {
				"isoform" : iso_info,
				"feature" :  splitline[2]
			}
			pos_gff_info.append(iso)
			prev_end = int(splitline[4])
			continue
		if position < int(splitline[3]) and position > prev_end:
			iso = {
				"isoform" : "none",
				"feature" : "intron"
			}
			pos_gff_info.append(iso)
			prev_end = int(splitline[4])
			continue
		else:
			continue

	return pos_gff_info


def get_info_return_dict ( gene, info_dict):
	"""get the genotypes for each position for each sample"""
	chrom = info_dict['chrom']
	start = info_dict['start']
	end = info_dict['end']

	provean_list = get_PROVEAN_scores(gene)
	if (provean_list == 1):
		provean_list = ['NA'] * 8

	vcf_R = get_vcf_reader()

	gene_gff = get_gene_gff(gene)

	gene_records = []
	for rec in vcf_R.fetch(chrom, start, end):
		iso = get_gene_gff_info(gene_gff, rec.POS)
		for sample in rec.samples:
			rw = {
				"gene" : gene,
				"sample" : sample.sample,
				"variety" : config.SAMPLE[sample.sample],
				"annotation" : info_dict['annotation'],
				"chromosome" : config.CHROM_FULL[chrom],
				"position" : rec.POS,
				"gene_feature_location" : iso,
				"start" : info_dict['start'],
				"end" : info_dict['end'],
				"reference" : rec.REF,
				"alternate" : str(rec.ALT[0]),
				"genotype" : sample['GT'],
				"SNPEFF_effect" : rec.INFO['SNPEFF_EFFECT'],
				"SNPEFF_FUNCTIONAL_CLASS" : rec.INFO['SNPEFF_FUNCTIONAL_CLASS'],
				"p_transcript_id" : provean_list[0],
				"p_minimumScore" : provean_list[1],
				"p_sumScore" : provean_list[2],
				"p_deleteriousCount" : provean_list[3],
				"p_proteinLength" : provean_list[4],
				"p_proportionDeleterious" : provean_list[5],
				"p_deleteriousMutations" : provean_list[6],
				"p_deleteriousScores" : provean_list[7]
			}
			gene_records.append(rw)

	gene_json = json.dumps(gene_records)
	return gene_json

def get_PROVEAN_scores (gene) :
	provean = open(config.PROVEAN, 'r')
	provean_info = []
	myregex = r"(.*)" + re.escape(gene) + r"(.*)"
	for line in provean:
		if re.match(myregex, line):
			provean_info.append(line)
	if (len(provean_info) == 0):
		return 1
	provean_info = provean_info[0].split('\n')[0]
	provean_list = provean_info.split('\t')
	return provean_list

###############################
#            Main             #

if __name__ == '__main__':
	file, gene = sys.argv
	
	info_line = get_MSU_info(gene)
	#print type(info_line)
	if (info_line == "Gene not found."):
		print 1
		sys.exit()
	info = get_start_stop(info_line)
	#gene_gff = get_gene_gff(gene)
	results = get_info_return_dict(gene, info)
	print results
	sys.stdout.flush()
