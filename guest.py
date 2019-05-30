#coding:utf-8

filename = 'txt_files\guest.txt'
while True:
	guest_name = input("Please enter your name :")
	print('Welcome '+ guest_name + ' !')
	with open(filename,'a') as file_object:
		file_object.write(guest_name+"\n")
	

