#coding:utf-8
filename = 'txt_files\pi_digits.txt'
with open(filename) as file_object:
		lines = file_object.readlines() # 逐行读取并存储在一个list

pi_string = ''
for line in lines:
	pi_string += line.strip() #去除两边的空白
print(pi_string)
print(len(pi_string))

birthday = input('Enter your birthday: ') #判断生日是否在pi里面
if birthday in pi_string:
	print('Your birthday is in Pi')
else:
	print('Your birthday is not in Pi')
		

	
	
