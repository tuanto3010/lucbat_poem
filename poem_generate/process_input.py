import os
import tachdau as tach

input_path=os.path.dirname(os.path.abspath(__file__))
input_folder=os.path.join(input_path,'data')
list_input_file= os.listdir(input_folder)
count=0
for file in list_input_file:
	count+=1
	path_to_file=os.path.join(input_folder,file)
	with open(path_to_file, encoding='utf-8') as f:
		data = f.read()
		for line in data.split('\n'):
			print(line)
			print(tach.validate_daucau(line))
	if(count==2):
		break

# if not os.path.exists('./model'):
#     os.makedirs('./model')#
# t = "Lưu Tuấn Anh"
# print(tach.convert(t))

# # tt = t.split(u" ")

# # print(tt)