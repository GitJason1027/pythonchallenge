#把网页最后的html改为zip，下载源文件channel.zip
import re
import zipfile

def process_num_6():
    with zipfile.ZipFile('channel.zip','r') as f:
        final = ''
        file_content = f.namelist()
        content = '90052'
        #print(content)
        while re.findall('(\d+)',content):
            num = re.findall('(\d+)',content)[0]
           # print(num)
            content = '{}.txt'.format(num)
            ff = f.getinfo(content)
            c = f.open(content,'r')
            content = str(c.read())
            #print(num,content,ff.comment)
            final+=bytes.decode(ff.comment)
    print(final)

if __name__ == '__main__':
	number = '90052'
	process_num_6()

#http://www.pythonchallenge.com/pc/def/hockey.html
#it's in the air. look at the letters. 
#http://www.pythonchallenge.com/pc/def/oxygen.html


