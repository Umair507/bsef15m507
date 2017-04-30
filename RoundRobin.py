process=[]
num_value=int(raw_input('How Many Processes You Want To Enter = '))
time_slice=int(raw_input('Enter The Time Slice = '))
for index in range(num_value):
	process.append([])
	process[index].append(raw_input('Process Name = '))
	process[index].append(int(raw_input('Process A.T = ')))
        process[index].append(int(raw_input('Process B.T = ')))
process_run=[]
process.sort(key=lambda process:process[1])
import Queue
ready=Queue
ready=ready.Queue()
temp_value=0
p_array=0
ready.put(process[p_array])
p_array+=1
print 'Roun_Robin --> Output'
while not ready.empty():
	process_run=ready.get()
	if process_run[2]>=time_slice:
		process_run[2]=process_run[2]-time_slice
		print process_run
		temp_value+=time_slice
		if p_array<num_value:
			while p_array<num_value:
				if process[p_array][1]<=temp_value:	
					ready.put(process[p_array])
				if p_array+1==num_value:
					p_array+=1
					break
				p_array+=1
		if process_run[2]!=0:
			ready.put(process_run)
	else:
		print process_run
		temp_value+=process_run[2]
		if p_array<num_value:
			while p_array<num_value:
				if process[p_array][1]<=temp_value:
					ready.put(process[p_array])
				if p_array+1==num_value:
					p_array+=1
					break
				p_array+=1
						
