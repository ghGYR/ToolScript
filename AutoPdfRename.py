from pdfminer import high_level
import os
while True:
    path=input("输入目录:")
    try:
        os.chdir(path)
        break
    except OSError as e:
        print(e)
files=os.listdir(path)
i=0
for file in files:
    print(file)
    try:
        text=high_level.extract_text(file,maxpages=1)
        name=text[0:100].split("\n")[0]
        if len(name)>8:
            ne=''
            for c in name:
                if c in ['.','\\','/',':','(',')']:
                    ne+="-"
                else:
                    ne+=c
            os.rename(file,name+".pdf")
    except:
        pass
    
#os.rename(old_file,new_file)
