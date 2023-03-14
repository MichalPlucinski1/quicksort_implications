import random
import time
from enum import Enum
import numpy as np
import matplotlib . pyplot as plot

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
	print("pivot of fr: ", pivot)
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
	print("pivot of m:",pivot)

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
	print("pivot of r:",pivot)
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
	for i in range(int(len/2)):
		arr.append(i)
	for i in range( len-1, int(len/2), -1):
		arr.append(i)

# Measuring time
def mTime(ar, sort, results):
	if sort == aSort.fr:
		start_time = time.time()
        fr_quick_sort(ar.copy())
        stop_time = time.time() - start_time
	
	elif sort == aSort.m:
		start_time = time.time()
        m_quick_sort(ar.copy())
        stop_time = time.time() - start_time
	
	elif sort == aSort.r:
		start_time = time.time()
        r_quick_sort(ar.copy())
        stop_time = time.time() - start_time
	
	results.append(stop_time)

######################### main ##############################################



def main():
    
	### settings of measure ###

	ar = []
	start_num = 10
	last_num = 20
    step = 2
    

	### bufored times ###
    vfr = []
    vm = []
    vr = []
    vTime = []
    

	### performing test ###
	for i in range(start_num, last_num, step):
	    tab_a_fill(ar, i)
	    vTime.append(i) #making y dimmension for plot
        print("Filling, len of arr: ", len(ar), " of ", last_num)

    	mTime(ar, aSort.fr, vfr)
    	mTime(ar, aSort.m, vm)
    	mTime(ar, aSort.r, vr)
    
        #print(sort.name,"  %s seconds " % (t))            
		del ar	    


    #fr
	array = [10, 7, 8, 9, 1, 5]
	fr_quick_sort(array, 0, len(array) - 1)
	print(f'Sorted array fr: {array}')

    #mid
	array1 = [10, 7, 8, 9, 1, 5]
	m_quick_sort(array1, 0, len(array1) - 1)
	print(f'Sorted array mid: {array1}')

    #rand
	array2 = [10, 7, 8, 9, 1, 5]
	r_quick_sort(array2, 0, len(array2) - 1)
	print(f'Sorted array rand: {array2}')

	

if __name__ == "__main__":
    main()
