#coding:utf-8
def count_words(filename):
	try:
		with open(filename) as f_obj:
			contents = f_obj.read()
	except FileNotFoundError:
		msg = "Sor,can not find the file : " + filename
		print(msg)
	else:
		words = contents.split()
		print(words[0:10])
		num_words = len(words)
		print("这个文件有 " + str(num_words) +" 个字")

filenames = ['txt_files/alice.txt','txt_files/sherlock.txt','gg.txt'] #源文件格式要注意
for filename in filenames:
	count_words(filename)
