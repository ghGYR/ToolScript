import os
import re


def doublication_index(s1='00:00:01,000 --> 00:00:06,000', s2='00:00:01,000 --> 00:00:06,000'):  # 判断两个时间区间的重合度
    time1 = []  # time1用来存储以h：m：s, ms格式的时间
    time2 = []  # time2用来存储以xxx s.yyy ms格式的时间
    time1.extend(s1.split(' --> '))
    time1.extend(s2.split(' --> '))
    for i in time1:
        split_time = i.split(':')
        calc_time = int(split_time[0]) * 3600 + int(split_time[1]) * 60 + int(split_time[2].split(',')[0]) + int(split_time[2].split(',')[1]) / 1000
        time2.append(calc_time)

    if time2[2] > time2[1] or time2[0] > time2[3]:
        return 0  # 不重合的情况，重合度0
    time2.sort()
    return (time2[2] - time2[1]) / (time2[3] - time2[0])

path = os.getcwd() + '/merge'  # 将工作路径设为 ./merge
sub_type = 'srt'  # 字幕类型，如srt，txt等

for file in os.listdir(path):
    if re.search(r"Chs\." + sub_type + '$', file):  # 首先寻找中文字幕文件
        print('正在处理文件：' + file)
        eng_file = file.replace('Chs', 'Eng')
        if os.path.isfile(eng_file):  # 判断英文文件是否存在
            with open(file, 'r') as f:
                chs = f.readlines()  # 读入中文字幕文件
            with open(eng_file, 'r') as f:
                eng = f.readlines()  # 读入英文字幕文件

            chs_time, eng_time = [], []  # 定义两个变量存储中文字幕和英文字幕时间轴的行序号
            for i in range(len(chs)):
                if re.search('^\d\d:\d\d:\d\d', chs[i]):
                    chs_time.append(i)
            for i in range(len(eng)):
                if re.search('^\d\d:\d\d:\d\d', eng[i]):
                    eng_time.append(i)
            # 首先根据中文字幕的时间轴寻找最匹配的英文字幕时间轴
            for i in range(len(chs_time) - 1):
                for j in range(len(eng_time) - 1):
                    if doublication_index(chs[chs_time[i]], eng[eng_time[j]]) > 0.5:
                        for xh in range(eng_time[j] + 1, eng_time[j + 1]-2):
                            print("0")
                            chs[chs_time[i + 1] - 3] += eng[xh]
            # 由于根据下一段时间轴判断字幕文件行数，因此最后一条字幕需要单独处理
            rows_chs, rows_eng = 0, 0
            while chs[chs_time[-1] + rows_chs] != '\n':
                rows_chs += 1
            while eng[eng_time[-1] + rows_eng] != '\n':
                rows_eng += 1
            for xh in range(1, rows_eng):
                chs[chs_time[-1] + rows_chs - 1] += eng[eng_time[-1] + xh]

            with open(file, 'w') as f:
                f.writelines(chs)