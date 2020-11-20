#finds duplicate numbers if they are duplicated over many lines in a file

import re

with open('url_list2.txt','r') as f:
    num_list = []

    #gets all numbers in file
    for line in f:
        temp = re.findall(r'\d+',line)
        for x in temp:
##                if temp.count(x) == 1:
                    num_list.append(x)

    f.close()


#gets all instances of duplicate numbers
dup_list = [x for x in num_list if num_list.count(x) > 2]

#gets list of duplicated numbers
final_list = []
[final_list.append(x) for x in dup_list if x not in final_list]

final_list.sort()
print('duplicate numbers: ',final_list)
