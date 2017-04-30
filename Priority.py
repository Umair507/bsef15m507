process=[]
num_value=(int(raw_input('How Many Processes You Want To Enter = ')))
temp_value=0
for index in range(num_value):
	process.append([])
	process[index].append(raw_input('Enter Process Name = '))
	process[index].append(int(raw_input('Process A.T = ')))
        process[index].append(int(raw_input('Process B.T = ')))
	process[index].append(int(raw_input('Process Priority # = ')))
	temp_value+=process[index][3]
process.sort(key=lambda process:process[1])
process.sort(key=lambda process:process[3])
print 'Priority Scheduling --> Output'
for index in range(num_value):
	print process[index][0]
	print ''
print 'Total B.T = ',temp_value
