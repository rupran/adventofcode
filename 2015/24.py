from operator import mul

used = []
results = []
min_res_len = 120

def find_smallest_set(data, index, part, target):
    global results, min_res_len
    if part == target:
        len_res = reduce(lambda x, y: x+y, used, 0) 
        if len_res < min_res_len:
            results = [used[:]]
            min_res_len = len_res
        elif len_res == min_res_len:
            results.append(used[:])
        return
    elif part > target:
        return
    elif index == len(data):
        return

    find_smallest_set(data, index+1, part, target)
    used[index] = 1
    find_smallest_set(data, index+1, part + data[index], target)
    used[index] = 0

def find_any_partitions_from_half(data, index, partial_sum, target):
    global results
    if partial_sum == target:
        results.append(used[:])
        return
    elif index == len(data):
        return

    find_smallest_set(data, index+1, partial_sum, target)
    used[index] = 1
    find_smallest_set(data, index+1, partial_sum + data[index], target)
    used[index] = 0

data = [1, 3, 5, 11, 13, 17, 19, 23, 29, 31, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113]

data = list(reversed(data))

print sum(data)
partial_sum = sum(data)/3
print partial_sum

for _ in data:
    used.append(0)

find_smallest_set(list(data), 0, 0, partial_sum)

res_list = []
min_qe = 0

for min_list in results:
    data_without = data[:]
    elems = []
    for idx in range(0, len(min_list)):
        if min_list[idx] == 1:
            elems.append(data[idx])
            data_without.remove(data[idx])

    results = []
#    find_any_partitions_from_half(data_without, 0, 0, partial_sum)
#    if len(results) == 0:
#        print "FAUL"
#        continue
#    else:
#        print "Works"
    
    qe = reduce(mul, elems, 1)
    if min_qe == 0 or min_qe > qe:
        min_qe = qe
        res_list = elems

print min_qe, res_list 
