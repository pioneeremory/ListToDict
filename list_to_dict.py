# This function converts lists to dictionaries

list1 = ['table', 'chair', 'rack', 'shelf']
list2 = [100,50,80,40]
combined_lists = {}

def list_to_dict(list1, list2):

    for item in list1:
        combined_lists.append(item)
    print(combined_lists)

