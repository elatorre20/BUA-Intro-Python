import random

def slow_sort(unsorted_list):
    while(true):
        if(unsorted_list == sorted(unsorted_list)):
            return(unsorted_list)
        else:
            unsorted_list.shuffle()
        
def minimum(a_list):
    x = a_list[0]
    for i in a_list:
        if i < x:
            x = i
    return x

def selection_sort(unsorted_list):
    sorted_list = []
    while(len(unsorted_list) > 0):
        sorted_list.append(minimum(unsorted_list))
        unsorted_list.remove(minimum(unsorted_list))
    return sorted_list
            
def gen_unsorted_list(length):
    unsorted_list = []
    for i in range(length):
        unsorted_list.append(random.randint(1,100))
    return unsorted_list
