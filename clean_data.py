file='all_lucbacpoem.txt'
with open(file, encoding='utf-8') as f:
	data = f.read()
for line in data.split('\n'):
	print(line)