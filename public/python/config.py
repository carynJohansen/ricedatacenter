# PYTHON IMPORTS

pyvcf = '/Users/caryn/Dropbox/Project_RiceGeneticVariation/database/vcf'

VCF='/Users/caryn/Dropbox/Project_OryzaDataCenter/bwa_msdr_MRE_F.vcf.gz'

DATABASE='/Users/caryn/Dropbox/Project_OryzaDataCenter/michael_04042016.db'

PROVEAN = '/Users/caryn/Dropbox/Project_OryzaDataCenter/simple_genes/data/Ines_provean_assemble.out'

# dictionary for interpreting chromosome

CHROM_DICT = {
	"01" : "Chr1",
	"02" : "Chr2",
	"03" : "Chr3",
	"04" : "Chr4",
	"05" : "Chr5",
	"06" : "Chr6",
	"07" : "Chr7",
	"08" : "Chr8",
	"09" : "Chr9",
	"10" : "Chr10",
	"11" : "Chr11",
	"12" : "Chr12"
}

CHROM_FULL = {
	"Chr1" : "Chromosome 1",
	"Chr2" : "Chromosome 2",
	"Chr3" : "Chromosome 3",
	"Chr4" : "Chromosome 4",
	"Chr5" : "Chromosome 5",
	"Chr6" : "Chromosome 6",
	"Chr7" : "Chromosome 7",
	"Chr8" : "Chromosome 8",
	"Chr9" : "Chromosome 9",
	"Chr10" : "Chromosome 10",
	"Chr11" : "Chromosome 11",
	"Chr12" : "Chromosome 12"
}

CHROM_INFO_PATH = {
	"01" : '/Users/caryn/Dropbox/Project_jsLearn/simple_genes/data/Chr1.dir/Chr1.locus_brief_info.7.0',
	"02" : '/Users/caryn/Dropbox/Project_jsLearn/simple_genes/data/Chr2.dir/Chr2.locus_brief_info.7.0',
	"03" : '/Users/caryn/Dropbox/Project_jsLearn/simple_genes/data/Chr3.dir/Chr3.locus_brief_info.7.0',
	"04" : '/Users/caryn/Dropbox/Project_jsLearn/simple_genes/data/Chr4.dir/Chr4.locus_brief_info.7.0',
	"05" : '/Users/caryn/Dropbox/Project_jsLearn/simple_genes/data/Chr5.dir/Chr5.locus_brief_info.7.0',
	"06" : '/Users/caryn/Dropbox/Project_jsLearn/simple_genes/data/Chr6.dir/Chr6.locus_brief_info.7.0',
	"07" : '/Users/caryn/Dropbox/Project_jsLearn/simple_genes/data/Chr7.dir/Chr7.locus_brief_info.7.0',
	"08" : '/Users/caryn/Dropbox/Project_jsLearn/simple_genes/data/Chr8.dir/Chr8.locus_brief_info.7.0',
	"09" : '/Users/caryn/Dropbox/Project_jsLearn/simple_genes/data/Chr9.dir/Chr9.locus_brief_info.7.0',
	"10" : '/Users/caryn/Dropbox/Project_jsLearn/simple_genes/data/Chr10.dir/Chr10.locus_brief_info.7.0',
	"11" : '/Users/caryn/Dropbox/Project_jsLearn/simple_genes/data/Chr11.dir/Chr11.locus_brief_info.7.0',
	"12" : '/Users/caryn/Dropbox/Project_jsLearn/simple_genes/data/Chr12.dir/Chr12.locus_brief_info.7.0'
}

GFF_PATH = {
	"01" : "/Users/caryn/Dropbox/Project_jsLearn/simple_genes/data/Chr1.dir/Chr1.gff3",
	"02" : "/Users/caryn/Dropbox/Project_jsLearn/simple_genes/data/Chr2.dir/Chr2.gff3",
	"03" : "/Users/caryn/Dropbox/Project_jsLearn/simple_genes/data/Chr3.dir/Chr3.gff3",
	"04" : "/Users/caryn/Dropbox/Project_jsLearn/simple_genes/data/Chr4.dir/Chr4.gff3",
	"05" : "/Users/caryn/Dropbox/Project_jsLearn/simple_genes/data/Chr5.dir/Chr5.gff3",
	"06" : "/Users/caryn/Dropbox/Project_jsLearn/simple_genes/data/Chr6.dir/Chr6.gff3",
	"07" : "/Users/caryn/Dropbox/Project_jsLearn/simple_genes/data/Chr7.dir/Chr7.gff3",
	"08" : "/Users/caryn/Dropbox/Project_jsLearn/simple_genes/data/Chr8.dir/Chr8.gff3",
	"09" : "/Users/caryn/Dropbox/Project_jsLearn/simple_genes/data/Chr9.dir/Chr9.gff3",
	"10" : "/Users/caryn/Dropbox/Project_jsLearn/simple_genes/data/Chr10.dir/Chr10.gff3",
	"11" : "/Users/caryn/Dropbox/Project_jsLearn/simple_genes/data/Chr11.dir/Chr11.gff3",
	"12" : "/Users/caryn/Dropbox/Project_jsLearn/simple_genes/data/Chr12.dir/Chr12.gff3"
}

# Rice Data

RICE_CATEGORY = {
	"IND" : "Indica",
	"AUS" : "Aus",
	"ARO" : "Aromatic",
	"TRJ" : "Tropical Japonica",
	"TEJ" : "Temperate Japonica",
	"ADM" : "Admixed",
	"TEJ/TRJ" : "Japonica (Temperate or Tropical)",
	"UKN" : "Unclassified",
	"AUS/IND" : "Aus or Indica"
}

SAMPLE = {
	"Sample_IRGC117281" : "Aswina",
	"Sample_IRGC6208" : "Chitraj (DA 23)",
	"Sample_IRGC8341" : "Dhola aman (lowland aman)",
	"Sample_IRGC38994" : "Bico Branco",
	"Sample_IRGC50448" : "Canela de Ferro",
	"Sample_IRGC8195" : "Kun-Min-Tsieh-Hunan",
	"Sample_IRGC117269" : "Li-Jiang-Xin- Tuan-Hei-Gu",
	"Sample_IRGC51400" : "Pa tou hung",
	"Sample_IRGC117272" : "Moroberekan",
	"Sample_IRGC9389" : "Amarelo",
	"Sample_IRGC12331" : "ARC 7229",
	"Sample_IRGC6331" : "CO 18",
	"Sample_IRGC117267" : "FR 13 A",
	"Sample_IRGC12894" : "Gompa 2",
	"Sample_IRGC9069" : "JC 148",
	"Sample_IRGC9070" : "JC 149",
	"Sample_IRGC9177" : "JC 91",
	"Sample_IRGC9175" : "JC 93",
	"Sample_IRGC6307" : "Jhona 349",
	"Sample_IRGC7919" : "MTU 9",
	"Sample_IRGC32559" : "NP 125",
	"Sample_IRGC5999" : "Pankhari 203",
	"Sample_IRGC53931" : "Sona Chur",
	"Sample_IRGC117278" : "Swarna",
	"Sample_IRGC74719" : "Uryee Boota",
	"Sample_IRTP1231" : "Nona Bokra",
	"Sample_IRTP24986" : "Pokkali",
	"Sample_IRGC43372" : "Cicih Beton",
	"Sample_IRGC19972" : "Keriting Tinggi",
	"Sample_IRGC66640" : "Si Adulo",
	"Sample_PandanWangi" : "Pandan Wangi",
	"Sample_IRGC15100" : "63-104",
	"Sample_IRGC12731" : "Nippon Bare",
	"Sample_IRGC14957" : "LAC 23",
	"Sample_IRGC71524" : "Gumpangar",
	"Sample_IRGC27869" : "Chahora 144",
	"Sample_IRGC28134" : "P 660",
	"Sample_IRGC73126" : "Tak Siah",
	"Sample_IRGC117268" : "IR 64-21",
	"Sample_IRGC26872" : "Binulawan",
	"Sample_IRGC8244" : "Davao",
	"Sample_IRGC67431" : "Dinolores",
	"Sample_IRGC8245" : "Macan Binundok",
	"Sample_IRGC8182" : "Malagkit Pirurutong",
	"Sample_Tadukan" : "Tadukan",
	"Os_23354" : "PINIDWA QAN QIPUGO BINAQUKUK",
	"Os_23359" : "PINIDWA QAN QIPUGO PINGKITAN",
	"Os_23361" : "PINIDWA QAN QIPUGO QINHAKELLOB",
	"Os_23362" : "PINIDWA QAN QIPUGO WALAY",
	"Os_44349" : "BONTOC RICE",
	"Os_47315" : "PINIDWA(NON-GLUT.)",
	"Os_47355" : "ONOY",
	"Os_60574" : "ALINNAWAN-DAYA'OT TINAWON",
	"Os_60589" : "IMPELLEPEL-DAYA'OT TINAWON",
	"Os_60590" : "INDONAAL-IPUGO TINAWON",
	"Os_60596" : "INNULA-IPUGO TINAWON",
	"Os_60598" : "LINAWANG-IPUGO(PINIDWA)",
	"Os_60605" : "PAUDAN-IPUGO TINAWON",
	"Os_71844" : "IMBOOKAN",
	"Os_8022" : "ENG-GUANG-GUANG-TINAWON RED",
	"Os_8043" : "IMBANNIGAN/TINAWON",
	"Os_8115" : "CHUMAJAG-TINAWON",
	"Os_8172" : "INGNGOPPOR-TINAWON",
	"Sample_Azucena-1" : "Azucena",
	"Sample_IRIS66333787" : "FL478",
	"Sample_IRTP201" : "IR29",
	"Sample_IRTP9542" : "IR58",
	"Sample_KinandangPuti" : "Kinandang Puti",
	"Sample_PSBRC1x" : "PSBRC_1",
	"Sample_IRGC16817" : "Hasawi (?)",
	"Sample_IRGC8952" : "Rathuwee",
	"Sample_IRGC51064" : "Sinna sithira Kali",
	"Sample_IRGC8196" : "Karasukara Surankasu",
	"Sample_IRGC8269" : "Nabeshi",
	"Sample_IRGC10430" : "Shinchiku Iku 103",
	"Sample_IRGC27748" : "Khao Dawk Mali 105",
	"Sample_IRGC5418" : "Sintane Diofor",
	"Tadukan" : "Tadukan",
	"Azucena" : "Azucena",
	"Kinandang_puti" : "Kinandang_puti",
	"Pandan_wangi" : "Pandan_wangi"
}