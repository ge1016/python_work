#coding:utf-8
filename = 'txt_files\pi_digits.txt'
with open(filename) as file_object:
		lines = file_object.readlines() # ���ж�ȡ���洢��һ��list

pi_string = ''
for line in lines:
	pi_string += line.strip() #ȥ�����ߵĿհ�
print(pi_string)
print(len(pi_string))

birthday = input('Enter your birthday: ') #�ж������Ƿ���pi����
if birthday in pi_string:
	print('Your birthday is in Pi')
else:
	print('Your birthday is not in Pi')
		

	
	
