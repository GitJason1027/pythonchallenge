def change(str):
	answer=''
	for i in str:
		if (ord(i)>=97) and (ord(i)<=122):
			num=ord(i)+2
			if num>=123:
				num = (ord(i)+2)-26
			temp = chr(num)
			answer = answer+temp
		else:answer = answer+i
	return answer

if __name__=='__main__':
	str='''g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.'''
	#str='www.pythonchallenge.com/pc/def/map'
	#method1
	#print(change(str))
	#method2
	intab='abcdefghijklmnopqrstuvwxyz'
	outtab='cdefghijklmnopqrstuvwxyzab'
	trantab=str.maketrans(intab, outtab)
	print(str.translate(trantab))

	'''
	i hope you didnt translate it by hand. 
	thats what computers are for. doing it in 
	by hand is inefficient and that's why this 
	text is so long. using string.maketrans() 
	is recommended. now apply on the url.

	http://www.pythonchallenge.com/pc/def/ocr
	'''
	