import string, os

#----------------------------------------------------------------
def reverse_compl_seq(strseq):
	strseq=strseq.upper()
	rc_strseq=strseq.translate(string.maketrans("ATCG", "TAGC"))[::-1]
	return rc_strseq;
	
def compl_seq(strseq):
	strseq=strseq.upper()
	c_strseq=strseq.translate(string.maketrans("ATCG", "TAGC"))
	return c_strseq;
	
def N_MIS(r,g):
	combo=[]
	if len(r)==len(g):
		combo=[r[i]+g[i] for i in range(len(r)) if r[i]!=g[i] and r[i] !="N" and g[i]!="N"]
		combo=[x for x in combo if x !="TC"]
	return len(combo);
	
#----------------------------------------------------------------

def methy_seq(r,g_long):
	H=['A','C','T']
	g_long=g_long.replace("_","")
	m_seq=str()
	xx="-"
	for i in range(len(r)):
		if r[i] not in ['C','T']:
			xx="-"
		elif r[i]=="T" and g_long[i+2]=="C": #(unmethylated):
			if g_long[i+3]=="G":
				xx="x"
			elif g_long[i+3] in H :
				if g_long[i+4]=="G":
					xx="y"
				elif g_long[i+4] in H :
					xx="z"

		elif r[i]=="C" and g_long[i+2]=="C": #(methylated):
			if g_long[i+3]=="G":
				xx="X"
			elif g_long[i+3] in H :
				if g_long[i+4]=="G":
					xx="Y"
				elif g_long[i+4] in H :
					xx="Z"
		else:
			xx="-"			
					
		m_seq=m_seq+xx
	return m_seq;



def mcounts(mseq,mlst,ulst):
	out_mlst=[mlst[0]+mseq.count("X"),mlst[1]+mseq.count("Y"),mlst[2]+mseq.count("Z")]
	out_ulst=[ulst[0]+mseq.count("x"),ulst[1]+mseq.count("y"),ulst[2]+mseq.count("z")]
	return out_mlst,out_ulst;

#-------------------------------------------------------------------------------------

# set a reasonable defaults
def find_location(program):
	def is_exe(fpath):
		return os.path.exists(fpath) and os.access(fpath, os.X_OK)
	for path in os.environ["PATH"].split(os.pathsep):	
		if is_exe(os.path.join(path, program)):
			return path

	return None
    
default_bowtie_path = find_location('bowtie') or "~/bowtie-0.12.7/"
