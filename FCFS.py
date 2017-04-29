process = []
num_value = int(raw_input('How Many Processes You want To Enter = '))
for index in range(num_value):
        process.append([])
        process[index].append(raw_input('Process Name = '))
        process[index].append(int(raw_input('Process A.T = ')))
        process[index].append(int(raw_input('Process B.T = ')))
        print ''
process.sort(key = lambda process:process[1])
print 'FCFS --> Output'
for index in range(num_value):
	print process[index][0]
	print ''


