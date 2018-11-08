def sort_to_max(origin_list):
   sort_list1 = origin_list[::1]
   sort_list2 = []
   for i in range(len(origin_list)):
       min = sort_list1[0]
       for k in sort_list1:
           min = k if min > k else min
       sort_list2.append(min)
       sort_list1.remove(min)
   return sort_list2

print(sort_to_max([2,10,-12,2.5,20,-11,4,4,0]))


