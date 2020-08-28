#coding=utf-8
'''
假设lrc歌词文件中，翻译与原文都是在同一个时刻上（应该都是吧
author: Tmn07
'''
import re
import sys
try:
	f = open(sys.argv[1], 'r')
except:
	print("Error")
	sys.exit()
data = f.read()
result = {}
times = []
for line in data.split('\n'):
	# 00:09.36
	match_list = re.findall('\[\d*?:\d*?\.\d*?]', line)
	if match_list:
		for m in match_list:

			tmp = result.get(m)
			if tmp:
				# lrc
				result[m] = tmp + "\n" + line[len(line)-line[::-1].index(']'):]
				# result[m] = tmp + "\n" + line[len(line)-line[::-1].index(']'):]
			else:
				result[m] = line[len(line)-line[::-1].index(']'):]
				times.append(m)
	else:
		continue

def maketime(start ,end):
	if start == 0:
		ss = '00:00:00,000'
	else:
		ss = "00:"+start[1:-1].replace('.',',')#+"0"
	se = "00:"+end[1:-1].replace('.',',')#+"0"
	return ss + " --> " + se

times.sort()
with open(sys.argv[1].replace("lrc","srt"), 'w') as f2:

	pretime = times[0]
	# for ind in range(1,len(times)):
	for ind in range(1,len(times)+1):
		f2.write(str(ind)+"\n")
		# 用于处理最后一条歌词信息
		if ind==len(times):
			f2.write(maketime(pretime, pretime)+"\n")
		else:
			f2.write(maketime(pretime, times[ind])+"\n")
			pretime = times[ind]
