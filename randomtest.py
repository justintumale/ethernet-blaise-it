#
# random number test for discrete event simulation
# drdan, 4/18/2016

import random

data_rate    = 40              #Mbit/s or bits per microsecond
arrival_rate = data_rate/400.0 #50-byte chunks per microsecond 
interval     = 1.0/arrival_rate   # average interfal between two chunks

sim_time = 0.0
rand_sum = 0.0
print ('Average inter-arrival time: '+str(interval))
for i in range(1,20):
    #print arrival time of next chunk
    randnum = random.random()
    rand_sum = rand_sum+randnum
    deltaT = 2.0*interval*randnum
    sim_time = sim_time+deltaT
    print ('  Packet '+str(i)+' arrives at '+str(sim_time))

print ('\n'+str(20*400)+ ' bits in '+str(sim_time)+' microseconds or '+str(8000/sim_time)+ 'bits per microsecond')
print ('Average random number: '+str(rand_sum/20))

