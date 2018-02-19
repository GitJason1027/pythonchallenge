import pickle
import requests

if __name__ == '__main__':
	f = open('banner.p','rb')
	data = pickle.load(f)
	final=''
	for i in data:
		for ii in i:
			for iii in range(ii[1]):
				final+=ii[0]
	print(final)
	f.close()
	#。。。画出来的图形貌似是channel，在ipython还可以看到大概形状
	#这里就看不出来了
	#http://www.pythonchallenge.com/pc/def/channel.html
