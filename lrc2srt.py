#coding=utf-8
import re
import sys


def readlrc(infile):
	data = infile.read()
	llrc = {}
	for line in data.split('\n'):
		match_list = re.findall('\[(\d*?:\d*?\.\d*?)]', line)
		for m in match_list:
			m.replace(".",",")
			if len(m.split(":"))<3:
				m="00:"+m
			string=line[len(line)-line[::-1].index(']'):]
			if llrc.get(m):
				llrc[m]+= "\\N" + string
			else:
				llrc[m]=string
	return llrc

def tran2srt(result):
	lsrt=[]
	times=sorted(result.keys())
	for ind in range(0,len(times)):
		i1=str(ind+1)+"\n"
		end=times[ind+1] if ind<len(times)-1 else times[ind]
		t2=times[ind]+" --> "+ end+"\n"
		s3=result[times[ind]]
		lsrt.append(i1+t2+s3)
	return "\n".join(lsrt)

if __name__=="__main__":
	try:
		with open(sys.argv[1], 'r') as f:
			srt=tran2srt(readlrc(f))
		with open(sys.argv[1].replace("lrc","srt"),"w") as f:
			f.write(srt)
		print("Finished")
	except:
		print("Error")