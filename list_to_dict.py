# This function converts lists to dictionaries

list1 = ['table', 'chair', 'rack', 'shelf']
list2 = [100,50,80,40]

def list_to_dict(list1, list2):
    combined_lists = {}
    for item in list1:
        combined_lists[item] = ''

    count = 0
        
    for key in combined_lists:
        combined_lists[key] = list2[count]
        count += 1
    return combined_lists

print(list_to_dict(list1, list2))




