from django.shortcuts import render # type: ignore
from .utils import bubble_sort, generate_array, selection, insertion, merge, quicksort, custom_algorithm_selector
import time

# bubble sort page
def sort(request):
    length = int(request.GET.get('length', 10))
    
    algo_one = int(request.GET.get('Algo1', 0))
    algo_two = int(request.GET.get('Algo2', 0))

    arr = generate_array(length)
    copy_arr = arr.copy()
    
    # first algo
    start_time = time.perf_counter()
    # bubble_sort(arr)
    algo_one_name = custom_algorithm_selector(algo_one, arr)
    elapsed_time = time.perf_counter() - start_time
    
    # second algo 
    start_time_second = time.perf_counter()
    # without_sorted = selection(copy_arr)
    algo_two_name = custom_algorithm_selector(algo_two, copy_arr)
    elapsed_time_second = time.perf_counter() - start_time_second
    
    # returning values to
    context = {'algo_one_name': algo_one_name, 'algo_two_name': algo_two_name, 'arr': arr, 'length': length, 'without_sorted': copy_arr, 'bubble_time': elapsed_time,'combination_time': elapsed_time_second}
    return render(request, 'sorting.html', context)

# insertion sort page
def insertion_sort(request):
    length = int(request.GET.get('length', 10))
    arr = generate_array(length)
    copy_arr = arr.copy()
    
    start_time = time.perf_counter()
    insertion(arr)
    elapsed_time = time.perf_counter() - start_time
    
    # second algo 
    start_time_second = time.perf_counter()
    without_sorted = selection(copy_arr)
    elapsed_time_second = time.perf_counter() - start_time_second
    
    
    context = {'arr': arr, 'length': length, 'without_sorted': without_sorted, 'bubble_time': elapsed_time,'combination_time': elapsed_time_second}
    return render(request, 'insertion.html', context)


# selection sort page
def selection_sort(request):
    length = int(request.GET.get('length', 10))
    arr = generate_array(length)
    copy_arr = arr.copy()
    start_time = time.perf_counter()
    selection(arr)
    elapsed_time = time.perf_counter() - start_time
    
    # second algo 
    start_time_second = time.perf_counter()
    without_sorted = selection(copy_arr)
    elapsed_time_second = time.perf_counter() - start_time_second
    context = {'arr': arr, 'length': length, 'without_sorted': without_sorted, 'bubble_time': elapsed_time,'combination_time': elapsed_time_second}
    return render(request, 'selection.html', context)


# merge sort page
def merge_sort(request):
    length = int(request.GET.get('length', 10))
    arr = generate_array(length)
    copy_arr = arr.copy()
    start_time = time.perf_counter()
    merge(arr)
    elapsed_time = time.perf_counter() - start_time
    
    # second algo 
    start_time_second = time.perf_counter()
    without_sorted = selection(copy_arr)
    elapsed_time_second = time.perf_counter() - start_time_second
    context = {'arr': arr, 'length': length, 'without_sorted': without_sorted, 'bubble_time': elapsed_time,'combination_time': elapsed_time_second}
    return render(request, 'merge.html', context)


# quick sort algorithm
def quick_sort(request):
    length = int(request.GET.get('length', 10))
    arr = generate_array(length)
    copy_arr = arr.copy()
    start_time = time.perf_counter()
    quicksort(arr, 0, len(arr)  - 1)
    elapsed_time = time.perf_counter() - start_time
    
    # second algo 
    start_time_second = time.perf_counter()
    without_sorted = selection(copy_arr)
    elapsed_time_second = time.perf_counter() - start_time_second
    context = {'arr': arr, 'length': length, 'without_sorted': without_sorted, 'bubble_time': elapsed_time,'combination_time': elapsed_time_second}
    return render(request, 'quick.html', context)


# custom comparision page
def custom_sort(request):
    length = int(request.GET.get('length', 0))
    arr = generate_array(length)
    copy_arr = arr.copy()
    start_time = time.perf_counter()
    bubble_sort(arr)
    elapsed_time = time.perf_counter() - start_time
    
    # second algo 
    start_time_second = time.perf_counter()
    without_sorted = selection(copy_arr)
    elapsed_time_second = time.perf_counter() - start_time_second
    context = {'arr': arr, 'length': length, 'without_sorted': without_sorted, 'bubble_time': elapsed_time,'combination_time': elapsed_time_second}
    return render(request, 'custom.html', context)

def contact_us(request):
    length = int(request.GET.get('length', 10))
    arr = generate_array(length)
    copy_arr = arr.copy()
    start_time = time.perf_counter()
    bubble_sort(arr)
    elapsed_time = time.perf_counter() - start_time
    
    # second algo 
    start_time_second = time.perf_counter()
    without_sorted = selection(copy_arr)
    elapsed_time_second = time.perf_counter() - start_time_second
    context = {'arr': arr, 'length': length, 'without_sorted': without_sorted, 'bubble_time': elapsed_time,'combination_time': elapsed_time_second}
    return render(request, 'contact_us.html', context)



def team(request):
    length = int(request.GET.get('length', 10))
    arr = generate_array(length)
    copy_arr = arr.copy()
    start_time = time.perf_counter()
    bubble_sort(arr)
    elapsed_time = time.perf_counter() - start_time
    
    # second algo 
    start_time_second = time.perf_counter()
    without_sorted = selection(copy_arr)
    elapsed_time_second = time.perf_counter() - start_time_second
    context = {'arr': arr, 'length': length, 'without_sorted': without_sorted, 'bubble_time': elapsed_time,'combination_time': elapsed_time_second}
    return render(request, 'team.html', context)