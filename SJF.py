process = []
burst_time=[]
num_value = int(raw_input('How Many Processes You Want To Enter = '))
arrival_time=(int(raw_input('Enter A.T = ')))
for index in range(num_value):
        process.append([])
        process[index].append(raw_input('Enter Process Name = '))
        burst_time.append(int(raw_input('Enter B.T = ')))
next_j=1
for index in range(num_value):
	temp_v=index
	for next_j in range(num_value):
		if burst_time[next_j]<burst_time[temp_v]:
			temp_v=next_j
                temp=burst_time[index]
                burst_time[index]=burst_time[temp_v]
                burst_time[temp_v]=temp
                temp=process[index]
                process[index]=process[temp_v]
                process[temp_v]=temp
print 'SJF --> Output'
for index in range(num_value):
        print process[index]
	print ''
