# -*- coding:utf-8*-
# 利用PyPDF2模块合并同一文件夹下的所有PDF文件，按文件索引数字顺序合并。
# 存放PDF文件的文件夹名字即输出文件名。
# 命令行参数，文件夹地址
import os
from PyPDF2 import PdfFileReader, PdfFileWriter
import time
import sys
# 使用os模块的walk函数，搜索出指定目录下的全部PDF文件
# 获取同一目录下的所有PDF文件的绝对路径
def getFileName(filedir):

    file_list = [os.path.join(root, filespath) \
                 for root, dirs, files in os.walk(filedir) \
                 for filespath in files \
                 if str(filespath).endswith('pdf')
                 ]
    return file_list if file_list else []

# 合并同一目录下的所有PDF文件
def MergePDF(filepath, outfile):

    output = PdfFileWriter()
    outputPages = 0
    pdf_fileName = getFileName(filepath)

    if pdf_fileName:
        pdf_fileName=sorted(pdf_fileName,key=lambda T:T.split("/")[-1])
        for pdf_file in pdf_fileName:
            print("Path：%s"%pdf_file)
            # 读取源PDF文件
            input = PdfFileReader(open(pdf_file, "rb"))
            # 获得源PDF文件中页面总数
            pageCount = input.getNumPages()
            outputPages += pageCount
            print("Page：%d"%pageCount)
            # 分别将page添加到输出output中
            for iPage in range(pageCount):
                output.addPage(input.getPage(iPage))
                
        print("Total Pages:%d."%outputPages)
        # 写入到目标PDF文件
        outputStream = open(os.path.join(filepath, outfile), "wb")
        output.write(outputStream)
        outputStream.close()
        print("Finished！")

    else:
        print("Found no files！")


if __name__=="__main__":
    time1 = time.time()
    file_dir = sys.argv[1]
    outfile = file_dir.split("/")[-1]+".pdf"
    MergePDF(file_dir, outfile)
    time2 = time.time()
    print('Cost time：%s s.' %(time2 - time1))
