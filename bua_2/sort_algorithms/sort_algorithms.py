import random, time

def gen_unsorted_list(length = 10, lower = 0, upper = 99):
    gen_list = [] #start with an empty list
    for i in range(length): #for length
        gen_list.append(random.randint(lower, upper)) #add a random int between lower and upper
    return gen_list #return the list

def permutation_sort(unsorted_list):
    start = time.perf_counter()
    sorted_list = unsorted_list.copy()
    while(True):
        random.shuffle(sorted_list) #shuffle the list
        #print(sorted_list)
        if(sorted_list == sorted(sorted_list)): #if the list is now sorted
            end = time.perf_counter()
            print("Total time: " + str((end-start)*1000) + "ms")
            return sorted_list #return the sorted list

def bubble_sort(unsorted_list):
    start = time.perf_counter()
    sorted_list = unsorted_list.copy()
    while(sorted_list != sorted(sorted_list)): #while the list is not sorted
        #print(sorted_list)
        for i in range(len(sorted_list)-1): #iterate over the list
            if(sorted_list[i] > sorted_list[i+1]): #if any two elements next to each other are out of order
                x = sorted_list[i] #swap them
                sorted_list[i] = sorted_list[i+1]
                sorted_list[i+1] = x
    end = time.perf_counter()
    print("Total time: " + str((end-start)*1000) + "ms")
    return sorted_list

def merge_sort(unsorted_list):
    #print(unsorted_list)
    if(len(unsorted_list) == 1): #if there is only one element, the list is sorted
        return(unsorted_list)
    else:
        half_length = int(len(unsorted_list)/2) 
        a = unsorted_list[:half_length] #split the list in half
        b = unsorted_list[half_length:]
        a = merge_sort(a) #recursively sort the halves
        b = merge_sort(b)
        sorted_list = []
        i = 0 #keep track of indices in each list
        j = 0
        while i < len(a) and j < len(b): #while there are still items in both lists
            if a[i] < b[j]: #compare the smallest item in each list
                sorted_list.append(a[i]) #add it to the sorted list
                i = i + 1 #increment the index for this list
            else:
                sorted_list.append(b[j])
                j = j + 1
        sorted_list = sorted_list + a[i:] # whichever list has items left in it, add those to the end
        sorted_list = sorted_list +b[j:]
        return(sorted_list)
    
def merge_sort_timed(unsorted_list): #helper function to time merge sort as it is recursive
    start = time.perf_counter()
    sorted_list = merge_sort(unsorted_list)
    end = time.perf_counter()
    print("Total time: " + str((end-start)*1000) + "ms")
    return sorted_list
            
