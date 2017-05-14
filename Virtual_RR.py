from collections import deque
process={1:[1,5,8,0,1,9],2:[5,9,6,1,7,6],3:[8,6,7,4,1,1],4:[8,9,8,6,9,7],5:[6,6,3,9,1,0]}
def queue_attach(time,process_key,Que=[]):
	index=0
	while(index<time):
		Que.append(process_key)
		index+=1
	return
def process_work(time,que=deque([]),process={},Que=[]):
	index=0
	count=0
	while index<len(Que):
		if process.get(Que[index])[3]<=time:
			que.append(Que[index])
			Que[index]=-1
			count+=1
		index+=1
	while count>0:
		Que.remove(-1)
		count-=1
	return		
Ready_Q=[]
in_out=[]
temp_in_out=[]
process_key=[1,2,3,4,5]
process_enter=[1,2,3,4,5]
In_Out_time=2
time=0
number=5
temp_t=3
wait_t=5
Aux_Q=[]
Ready=deque([])
Aux=deque([])
while number>0:
	process_work(time,Ready,process,process_enter) 
	process_work(time,Ready,process,temp_in_out)
	process_work(time,Aux,process,in_out) 
	if not (Ready or Aux):
		Ready_Q.append(-1)
		time=time+1
	elif (Aux):
		element=Aux.popleft()
		if process.get(element)[2]<=process.get(element)[5]:
			time=time+process.get(element)[2]
			queue_attach(process.get(element)[2],element,Ready_Q)
			process.get(element)[2]=0
			number-=1
			print '==> Process',element,'==> T.A.T=',time-process.get(element)[0]
		else:
			time=process.get(element)[5]+time
			queue_attach(process.get(element)[5],element,Ready_Q)
			process.get(element)[2]=process.get(element)[2]-process.get(element)[5]
			process.get(element)[4]=process.get(element)[4]-process.get(element)[5]
			process.get(element)[5]=temp_t
			process_work(time,Ready,process,process_enter) 
			process_work(time,Ready,process,temp_in_out)
			process_work(time,Aux,process,in_out)
			Ready.append(element)
	elif (Ready):
		element=Ready.popleft()
		if process.get(element)[4]==-1:
			if process.get(element)[2]<=temp_t:
				time=time+process.get(element)[2]
				queue_attach(process.get(element)[2],element,Ready_Q)
				process.get(element)[2]=0
				number-=1
				print '==> Process',element,'==> T.A.T =',time-process.get(element)[0]
			else:
				time=time+temp_t
				queue_attach(temp_t,element,Ready_Q)
				process.get(element)[2]=process.get(element)[2]-temp_t
				process_work(time,Ready,process,process_enter) 
				process_work(time,Ready,process,temp_in_out)
				process_work(time,Aux,process,in_out) 
				Ready.append(element)
		else:
			if process.get(element)[2]<=process.get(element)[4]:
				if process.get(element)[2]<=temp_t:
					time=time+process.get(element)[2]
					queue_attach(process.get(element)[2],element,Ready_Q)
					process.get(element)[2]=0
					number-=1
					print '==> Process',element,'==> T.A.T =',time-process.get(element)[0]
				else:
					time=time+temp_t
					queue_attach(temp_t,element,Ready_Q)
					process.get(element)[2]=process.get(element)[2]-temp_t
					process.get(element)[4]=process.get(element)[4]-temp_t
					process_work(time,Ready,process,process_enter) 
					process_work(time,Aux,process,temp_in_out) 
					Ready.append(element)
print Ready_Q
