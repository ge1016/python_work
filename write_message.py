#coding:utf-8
filename = 'txt_files\programming.txt' #ͬʱ�������ļ�
with open(filename,'w') as file_object:
	file_object.write("I love programming.\n")
	file_object.write("I love tiki.\n")
	
with open(filename,'a') as file_object: #�����µ�����
	file_object.write("I love China.\n")
	file_object.write("I love Taipei.\n")

with open(filename) as file_object:
	lines = file_object.readlines()
for line in lines:
	print(line.strip())
