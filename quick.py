import random
import time
from enum import Enum
import numpy as np
import matplotlib . pyplot as plot
import sys
import threading

threading.stack_size(67108864)
sys.setrecursionlimit(2 ** 20)


### enum for sorts ###
class aSort(Enum):
    fr = 1
    m = 2
    r = 3


######################### selecting index of rightmost #########################

# Function to find the partition position
def fr_partition(array, low, high):

	# Choose the rightmost element as pivot
	pivot = array[high]
	#print("pivot of fr: ", pivot)
	# Pointer for greater element
	i = low - 1

	# Traverse through all elements
	# compare each element with pivot
	for j in range(low, high):
		if array[j] <= pivot:
			# If element smaller than pivot is found
			# swap it with the greater element pointed by i
			i = i + 1

			# Swapping element at i with element at j
			(array[i], array[j]) = (array[j], array[i])

	# Swap the pivot element with
	# e greater element specified by i
	(array[i + 1], array[high]) = (array[high], array[i + 1])

	# Return the position from where partition is done
	return i + 1

# Function to perform quicksort
def fr_quick_sort(array, low, high):
	if low < high:

		# Find pivot element such that
		# element smaller than pivot are on the left
		# element greater than pivot are on the right
		pi = fr_partition(array, low, high)

		# Recursive call on the left of pivot
		fr_quick_sort(array, low, pi - 1)

		# Recursive call on the right of pivot
		fr_quick_sort(array, pi + 1, high)


######################### selecting index of middle #########################


# Function to find the partition position
def m_partition(array, low, high):

	# Choose the rightmost element as pivot
	l = int((high + low) / 2)
	pivot = array[l]
	#print("pivot of m:",pivot)

	# Pointer for greater element
	i = low - 1

	# Traverse through all elements
	# compare each element with pivot
	for j in range(low, high):
		if array[j] <= pivot:
			# If element smaller than pivot is found
			# swap it with the greater element pointed by i
			i = i + 1

			# Swapping element at i with element at j
			(array[i], array[j]) = (array[j], array[i])

	# Swap the pivot element with
	# e greater element specified by i
	(array[i + 1], array[high]) = (array[high], array[i + 1])

	# Return the position from where partition is done
	return i + 1

# Function to perform quicksort
def m_quick_sort(array, low, high):
	if low < high:

		# Find pivot element such that
		# element smaller than pivot are on the left
		# element greater than pivot are on the right
		pi = m_partition(array, low, high)

		# Recursive call on the left of pivot
		m_quick_sort(array, low, pi - 1)

		# Recursive call on the right of pivot
		m_quick_sort(array, pi + 1, high)

######################### selecting index of random #########################

# Function to find the partition position
def r_partition(array, low, high):

	# Choose the rightmost element as pivot
	rand = random.randrange(low, high)
	pivot = array[rand]
	#print("pivot of r:",pivot)
	# Pointer for greater element
	i = low - 1

	# Traverse through all elements
	# compare each element with pivot
	for j in range(low, high):
		if array[j] <= pivot:
			# If element smaller than pivot is found
			# swap it with the greater element pointed by i
			i = i + 1

			# Swapping element at i with element at j
			(array[i], array[j]) = (array[j], array[i])

	# Swap the pivot element with
	# e greater element specified by i
	(array[i + 1], array[high]) = (array[high], array[i + 1])

	# Return the position from where partition is done
	return i + 1

# Function to perform quicksort
def r_quick_sort(array, low, high):
	if low < high:

		# Find pivot element such that
		# element smaller than pivot are on the left
		# element greater than pivot are on the right
		pi = r_partition(array, low, high)

		# Recursive call on the left of pivot
		r_quick_sort(array, low, pi - 1)

		# Recursive call on the right of pivot
		r_quick_sort(array, pi + 1, high)

######################### usage functions ###################################

# FILLING TAB
def tab_a_fill(arr, len):
	
	for i in range(0, len , 2):
		arr.append(i)

	for i in range(len - 1, 0, -2):
		arr.append(i)
    

# Measuring time
def mTime(ar, sort, results):
	if sort == aSort.fr:
		start_time = time.time()
		fr_quick_sort(ar.copy(), 0, len(ar) - 1)
		stop_time = time.time() - start_time
	
	elif sort == aSort.m:
		start_time = time.time()
		m_quick_sort(ar.copy(), 0, len(ar) - 1)
		stop_time = time.time() - start_time
	
	elif sort == aSort.r:
		start_time = time.time()
		r_quick_sort(ar.copy(), 0, len(ar) - 1)
		stop_time = time.time() - start_time
	
	results.append(stop_time)



# Making graphs
def plotting(vfr,vm,vr,vTime):
    #linear
    plot.subplot(1, 2, 1)
    plot.plot(vTime, vfr, vTime, vm, vTime, vr)
    plot.title("linear")
    plot.xlabel('number of sorts')
    plot.ylabel('time[s]')
    plot.legend(["right","mediana","random"])
    plot.grid(True)

    #logarithm
    plot.subplot(1, 2, 2)
    plot.plot(vTime, vfr, vTime, vm, vTime, vr)
    plot.yscale('log')
    plot.title(str('log'))
    plot.xlabel('number of sorts')
    plot.ylabel('time[s]')
    plot.legend(["right","mediana","random"])
    plot.grid(True) 
    


######################### main ##############################################



def main():
    
	### settings of measure ###

	
	start_num = 20
	last_num = 24
	step = 2
    

	### bufored times ###
	vfr = []
	vm = []
	vr = []
	vTime = []
    

	### performing test ###
	for i in range(start_num, last_num + 1, step):
		ar = []
		tab_a_fill(ar, i)
		vTime.append(i) #making y dimmension for plot
		print("Filling, len of arr: ", len(ar), " of ", last_num)
		print("i: ", i, "ar: ", ar)

		
		r_quick_sort(ar, 0, len(ar) - 1)
		print("ar after sort: ", ar)

		#mTime(ar, aSort.fr, vfr)
		#mTime(ar, aSort.m, vm)
		#mTime(ar, aSort.r, vr)
    
        #print(sort.name,"  %s seconds " % (t))            
		del ar	 

	#plotting(vfr, vm, vr, vTime)
	#plot.show()

	

if __name__ == "__main__":
    thread = threading.Thread(target=main) 
    thread.start()
