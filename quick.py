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

#################### sorts ####################
def partition(A, left_index, right_index):
    pivot = A[left_index]
    i = left_index + 1
    for j in range(left_index + 1, right_index):
        if A[j] < pivot:
            A[j], A[i] = A[i], A[j]
            i += 1
    A[left_index], A[i - 1] = A[i - 1], A[left_index]
    return i - 1


def quick_sort_random(A, left, right):
    if left < right:
        pivot = random.randint(left, right - 1)
        A[pivot], A[left] = (
            A[left],
            A[pivot],
        )  # switches the pivot with the left most bound
        pivot_index = partition(A, left, right)
        quick_sort_random(
            A, left, pivot_index
        )  # recursive quicksort to the left of the pivot point
        quick_sort_random(
            A, pivot_index + 1, right
        )  # recursive quicksort to the right of the pivot point


def quick_sort_right(A, left, right):
    if left < right:
        pivot = right-1
        A[pivot], A[left] = (
            A[left],
            A[pivot],
        )  # switches the pivot with the left most bound
        pivot_index = partition(A, left, right)
        quick_sort_right(
            A, left, pivot_index
        )  # recursive quicksort to the left of the pivot point
        quick_sort_right(
            A, pivot_index + 1, right
        )  # recursive quicksort to the right of the pivot point


def quick_sort_medium(A, left, right):
    if left < right:
        pivot = (left + right)//2
        A[pivot], A[left] = (
            A[left],
            A[pivot],
        )  # switches the pivot with the left most bound
        pivot_index = partition(A, left, right)
        quick_sort_medium(
            A, left, pivot_index
        )  # recursive quicksort to the left of the pivot point
        quick_sort_medium(
            A, pivot_index + 1, right
        )  # recursive quicksort to the right of the pivot point


######################### usage functions ###################################

# FILLING TAB
def tab_a_fill(arr, len):
	
	for i in range(0, len , 2):
		arr.append(i)

	for i in range(len - 1, 0, -2):
		arr.append(i)
    

# Measuring time
def mTime(ar, mysort, results):
    mytime = 0
    for i in range(0,3):
        start_time = time.time()
        mysort(ar.copy(), 0, len(ar) - 1)
        mytime += time.time() - start_time
    results.append(mytime/5)



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

	
	start_num = 2000
	last_num = 3500
	step = 100
    

	### bufored times ###
	vfr = []
	vm = []
	vr = []
	vTime = []
    

	vfr1 = []
	vm1 = []
	vr1 = []
        
	vfr2 = []
	vm2= []
	vr2 = []
        
	vfr3 = []
	vm3 = []
	vr3 = []
	### performing test ###
	"""
	for i in range(start_num, last_num + 1, step):
		ar = []
		tab_a_fill(ar, i)
		vTime.append(i) #making y dimmension for plot
		print("Filling, len of arr: ", len(ar), " of ", last_num)


		mTime(ar, quick_sort_right , vfr)
		mTime(ar, quick_sort_medium, vm)
		mTime(ar, quick_sort_random, vr)
          """      
	for i in range(start_num, last_num + 1, step):
		ar = []
		tab_a_fill(ar, i)
		vTime.append(i) #making y dimmension for plot
		print("Filling, len of arr: ", len(ar), " of ", last_num)


		mTime(ar, quick_sort_right , vfr1)
		mTime(ar, quick_sort_medium, vm1)
		mTime(ar, quick_sort_random, vr1)
    
	for i in range(start_num, last_num + 1, step):
		ar = []
		tab_a_fill(ar, i)
		#vTime.append(i) #making y dimmension for plot
		print("Filling, len of arr: ", len(ar), " of ", last_num)


		mTime(ar, quick_sort_right , vfr2)
		mTime(ar, quick_sort_medium, vm2)
		mTime(ar, quick_sort_random, vr2)
    

	for i in range(start_num, last_num + 1, step):
		ar = []
		tab_a_fill(ar, i)
		#vTime.append(i) #making y dimmension for plot
		print("Filling, len of arr: ", len(ar), " of ", last_num)


		mTime(ar, quick_sort_right , vfr3)
		mTime(ar, quick_sort_medium, vm3)
		mTime(ar, quick_sort_random, vr3)
    
		del ar
	for i in range(0, len(vfr1)):
		vfr.append((vfr1[i] + vfr2[i] + vfr3[i])/3)
		vm.append((vm1[i] + vm2[i] + vm3[i])/3)
		vr.append((vr1[i] + vr2[i] + vr3[i])/3)
	print("vfr: ", vfr)
	print("vfr1: ", vfr1)
	
	print("len:" ,len(vTime), "len V:", len(vfr1))
	plotting(vfr, vm, vr, vTime)
	plot.show()

	

if __name__ == "__main__":
    thread = threading.Thread(target=main) 
    thread.start()
