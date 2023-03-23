
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